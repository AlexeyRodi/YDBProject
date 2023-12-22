import ydb

def blocking_query(session, query):
  return session.transaction().execute(
    query,
    commit_tx = True,
    settings = ydb.BaseRequestSettings().with_timeout(3).with_operation_timeout(2)
  )

class Buyers_reader:

    def select_all_buyers(self, session):
      query = '''SELECT * FROM buyers;''';
      return blocking_query(session, query)

    def buyers_with_purchase(self,session):
      query = '''SELECT buyer.id as id, buyer.full_name as full_name, buyer.phone_number as phone_number, coalesce(purchase_id, 0) as purch,
      FROM buyers buyer left join purchase purch on buyer.purchase_id = purch.id;'''
      return blocking_query(session,query)
        
reader = Buyers_reader()