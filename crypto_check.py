import re
import pprint
import yan_web_page_download
import yan_web_page_batch_download

re_page_attributes = [
	re.compile(r'Transaction Receipt Status</div><div[^<>]*?><!---->\s*(?P<transaction_receipt_status>[^<>]*?)\s*</div>',flags = re.DOTALL),
	re.compile(r'Included in Block</div><div [^<>]*?><a href="/[A-z]+/block/(?P<included_in_block>[\d+]*?)"',flags = re.DOTALL),
	re.compile(r'>Type</div><div [^<>]*?>(?P<type>[^<>]*?)<',flags = re.DOTALL),
	re.compile(r'>Time</div><div [^<>]*?>(?P<time>[\d\-\:\s]*?)<',flags = re.DOTALL),
	re.compile(r'"from"\:"(?P<from_address>[^\"]*?)","to"\:"(?P<to_address>[^\"]*?)","value"\:"(?P<value>[^\"]*?)"}',flags = re.DOTALL),
	re.compile(r'<a href="/[A-z]+/token/[^\/\"]*?" title="(?P<token>[^\"]*?)"',flags = re.DOTALL),
	re.compile(r'>Energy Fee</div><div [^<>]*?>\s*(?P<energy_fee>[^<>]*?)\s*<',flags = re.DOTALL),
	re.compile(r'>Transaction Fees</div><div [^<>]*?>(?P<transaction_fee>[^<>]*?)<',flags = re.DOTALL),
]

def query_by_transaction_id(
	transaction_id,
	):
	output = {}
	page_url = 'https://trx.tokenview.com/en/tx/{}'.format(transaction_id)
	tokenview_html = yan_web_page_download.download_page_from_url(
		page_url = page_url,
		curl_file = 'tokenview_curl.sh',
		redirect = True)
	for r in re_page_attributes:
		for m in re.finditer(r, tokenview_html):
			output.update(m.groupdict())
	return output


'''
result = query_by_transaction_id(
	'da1d4e4787cf50e8e6c24865573ced6ec8d896982c4036df4cbe26e673da31ab'
	)

pprint.pprint(result)

result = query_by_transaction_id(
	'da1d4e4787cf50e8e6c24865573ced6ec8d896982c4036df4cbe26e673da31ac'
	)

pprint.pprint(result)
'''

######

'''

re1 = re.compile(
	r'.{0,200}4.40528 TRX.{0,200}',
	flags = re.DOTALL,
	)


for m in re.finditer(
	re1,
	tokenview_html,
	):
	print(m.group())
	print('\n\n\n')

'''