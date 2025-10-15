from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from typing import Optional
from app.schemas.query_schema import QueryRequest, QueryResponse
from app.controllers.query_controller import QueryController
from app.dependencies.service_deps import get_query_controller
from app.core.logging import get_logger


logger = get_logger(__name__)
router = APIRouter(prefix="/api/v1", tags=["query"])


@router.post("/parse", response_model=QueryResponse)
async def parse_query(
    request: QueryRequest,
    controller: QueryController = Depends(get_query_controller)
) -> QueryResponse:
    """
    Parse a Lucene query and return deterministic text, narrative text, and AST
    
    - **query**: Lucene query string to parse
    """
    try:
        logger.info(f"Received parse request")
        return controller.parse_query(request)
    except ValueError as e:
        logger.error(f"Bad request: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Internal error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/parse-file", response_model=QueryResponse)
async def parse_query_from_file(
    file: UploadFile = File(...),
    controller: QueryController = Depends(get_query_controller)
) -> QueryResponse:
    """
    Parse a Lucene query from a text file
    
    - **file**: Text file containing the Lucene query
    """
    try:
        logger.info(f"Received parse-file request: {file.filename}")
        
        content = await file.read()
        query_text = content.decode('utf-8').strip()
        
        if not query_text:
            raise ValueError("File is empty or contains only whitespace")
        
        request = QueryRequest(query=query_text)
        
        return controller.parse_query(request)
        
    except UnicodeDecodeError:
        logger.error("Failed to decode file as UTF-8")
        raise HTTPException(status_code=400, detail="File must be UTF-8 encoded text")
    except ValueError as e:
        logger.error(f"Bad request: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Internal error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
