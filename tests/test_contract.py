import ast,pathlib,re
P=pathlib.Path(__file__).parents[1]/'contracts'/'contract.py'
S=P.read_text(encoding='utf-8')
def test_contract_parses():ast.parse(S)
def test_surface():
 for name in ('mount_reel','light_reel','mount_patch','get_reel'):assert f'def {name}' in S
def test_source_binding_and_repair_preservation():
 assert 'hashlib.sha256' in S and "expected[0],'',expected[2]" in S
 assert "digest!=expected[i]" in S and "r.owner!=gl.message.sender_address" in S
def test_closed_outcomes_and_backstop():
 assert all(x in S for x in ('READY','REPAIR','BLOCKED','MISSING_DIALOGUE','SOUND_CUE_GAP'))
 assert "verdict=='READY' and (coverage<95 or indexes or codes)" in S
def test_validator_refetches():
 body=re.search(r'def _audit\(.*?\n @gl.public.write',S,re.S).group(0)
 assert 'gl.nondet.web.get' in body and 'prompt_comparative' in body
