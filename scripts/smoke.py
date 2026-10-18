import json,os,re,time
from genlayer_py import create_client,create_account
from genlayer_py.chains import studionet
import genlayer_py.contracts.actions as contract_actions
def compatible_calldata(method=None,args=None,kwargs=None):
 out={}
 if method is not None:out['method']=method
 if args:out['args']=args
 if kwargs:out['kwargs']=kwargs
 return out
contract_actions.make_calldata_object=compatible_calldata
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)));WORKSPACE=os.path.abspath(os.path.join(ROOT,'..','..','..','..'))
def value(name):
 text=open(os.path.join(WORKSPACE,'accounts.env'),encoding='utf-8').read();return re.search(rf'^\s*{name}\s*=\s*"?([^"\r\n]+)',text,re.M).group(1).strip()
account=create_account(account_private_key=value('ACCOUNT_3_GENLAYER_PRIVATE_KEY'));client=create_client(chain=studionet,account=account);dep=json.load(open(os.path.join(ROOT,'deployment.json')));address=dep['contract'];record='LANTERN-'+str(int(time.time()));base='https://raw.githubusercontent.com/sanshos1/caption-lantern/main/evidence/'
if compatible_calldata('probe',[])!={'method':'probe'}:raise SystemExit('calldata compatibility check failed')
def write(name,args):
 tx=client.write_contract(address=address,function_name=name,args=args);print(name+'Tx',tx,flush=True);receipt=client.wait_for_transaction_receipt(transaction_hash=tx,wait_until='finalized',retries=180,interval=5000,full_transaction=True);leaders=receipt.get('consensus_data',{}).get('leader_receipt')or[];leaders=[leaders] if isinstance(leaders,dict) else leaders
 if receipt.get('result_name')!='MAJORITY_AGREE' or not any(x.get('execution_result')=='SUCCESS' for x in leaders):raise SystemExit(name+' failed')
 return str(tx)
txs={'mount':write('mount_reel',[record,'Lantern Desk orientation','English',base+'demo-transcript.txt',base+'demo-captions.vtt',base+'demo-standard.txt']),'audit':write('light_reel',[record]),'patch':write('mount_patch',[record,base+'demo-patch.vtt'])}
stored=client.read_contract(address=address,function_name='get_reel',args=[record]);audit=stored.get('audit',{})
if stored.get('state')!='PATCHED' or audit.get('source_round')!='PATCH':raise SystemExit('canonical readback mismatch')
out={'recordId':record,'contractAddress':address,'transactions':txs,'state':stored.get('state'),'verdict':audit.get('verdict'),'coverage':audit.get('coverage'),'sourceRound':audit.get('source_round'),'readback':stored};os.makedirs(os.path.join(ROOT,'evidence'),exist_ok=True);open(os.path.join(ROOT,'evidence','live-run.json'),'w',encoding='utf-8').write(json.dumps(out,indent=2));print(json.dumps(out),flush=True)
