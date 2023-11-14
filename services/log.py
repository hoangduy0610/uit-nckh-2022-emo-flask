from repositories.log import getLogs

from datetime import datetime
from repositories.log import getLogs

import pytz

def query_logs(params):
    logs = getLogs()
    if logs is None:
        return {
            'status': False,
            'message': 'No logs found',
            'code': 404
        }
    if 'student_id' in params:
        logs = [log for log in logs if log.student_id == params['student_id']]
    if 'status' in params:
        logs = [log for log in logs if log.status == int(params['status'])]
    if 'date' in params:
        logs = [log for log in logs if log.created_at == params['date']]
    if 'from_date' in params and 'to_date' in params:
        timezone = pytz.timezone('Asia/Ho_Chi_Minh') # replace with your desired timezone
        from_date = datetime.strptime(params['from_date'] + ' 00:00:00', '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone)
        to_date = datetime.strptime(params['to_date'] + ' 23:59:59', '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone)
        logs = [log for log in logs if from_date <= log.created_at and log.created_at <= to_date]
    return {
        'status': True,
        'message': 'Successfully retrieved',
        'code': 200,
        'data': [log.serialize() for log in logs]
    }