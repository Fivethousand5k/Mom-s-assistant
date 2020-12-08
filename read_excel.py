import  xlrd
import datetime
from utils import *
from xlrd import xldate_as_tuple

def handler_excel(filename=None,time_range=3):
    # 打开文件
    workbook = xlrd.open_workbook(filename)
    index = workbook.sheet_names()[0]
    sheet2 = workbook.sheet_by_name(index)
    msg_dict={}
    result_dict={}
    # 遍历
    nrows = sheet2.nrows
    for i in range(0,nrows):
        row=sheet2.row_values(i)
        card_id,name,transaction_type,num,u_price,total,time,contractor,refers_num,co_bank=int(row[2]),row[3],row[8],row[10],row[11],row[12],row[13],row[4],row[15],row[16]
        time=time_parser(time)
        if card_id not in msg_dict:
            msg_dict[card_id]=[[name,transaction_type,num,u_price,total,time,contractor,refers_num,co_bank]]
        else:

            msg_dict[card_id].append([name,transaction_type,num,u_price,total,time,contractor,refers_num,co_bank])

    for kv in msg_dict.items():
        key,msg=kv[0],kv[1]

        if len(msg)>1:
            last_time='0001-01-01 00:00:00'
            last_buy_tuple=None
            for box in msg:
                time=box[5]
                transaction_type=box[1]
                name=box[0]
                if time_diff(time,last_time)<=time_range and transaction_type == "客户卖出":
                    if (key,name) not in result_dict:
                        result_dict[(key,name)]={last_buy_tuple: [box]}
                    else:
                        if last_buy_tuple in result_dict[(key,name)]:
                             result_dict[(key,name)][last_buy_tuple].append(box)
                        else:
                            result_dict[(key,name)][last_buy_tuple]=[box]
                if transaction_type == "客户买入" :
                    last_time=time
                    last_buy_tuple=tuple(box)

    return result_dict



if __name__ == '__main__':
    print(handler_excel('data/test2.xlsx'))