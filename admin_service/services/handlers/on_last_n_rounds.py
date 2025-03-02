from fastapi.responses import JSONResponse
from services.rounds_service import rounds_service
from utils.logger import logger
from utils.time_utils import convert_to_non_utc_time


async def execute(n: int):
    try:
        data, status_code = await rounds_service.last_n_rounds(n)

        if data.get('rounds', None) is not None:
            for index, round_dict in enumerate(data['rounds']):
                data['rounds'][index]['start_timestamp'] = convert_to_non_utc_time(
                    round_dict['start_timestamp']
                )
                data['rounds'][index]['end_timestamp'] = convert_to_non_utc_time(
                    round_dict['end_timestamp']
                )
            logger.info(f"Found {len(data['rounds'])} rounds")

        return JSONResponse(status_code=status_code, content=data)
    except Exception as e:
        logger.error(f'Failed to get last {n} rounds: {str(e)}', exc_info=True)
        return JSONResponse(status_code=500, content={'error': str(e)})
