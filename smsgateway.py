import json
def sms_reply():   
    data = str(request.vars.data)
    
    if data=='':
        res_data = {'status': 'Faild', 'ret_str': 'Required All'}
    else:
        cid="TCL"
        number=data.split('\n')[0].strip()
        from_number=number.split(':')[1].strip()
        message=data.split('\n')[1].strip()
        insertSql="INSERT INTO inbox (cid,from_number,message) values('"+str(cid)+"','"+str(from_number)+"','"+str(message)+"')"
        db.executesql(insertSql)
        res_data={
                'status': '200',
                'from_number': from_number,
                'message': message,
                }                
    data=response.json(res_data)
    return data
        