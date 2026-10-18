# Caption Lantern

_Screening note 01: accessibility defects should appear at the cue where they happen._

Mount one transcript, one caption track, and one public captioning standard. Caption Lantern freezes their exact bytes before independent GenLayer validators compare the track cue by cue. The stored reading is deliberately small: `READY`, `REPAIR`, or `BLOCKED`; a coverage percentage; exact cue indexes; and closed issue codes.

## What the light reveals

The browser is a projection booth, not a contract-argument form. A visitor assembles the reel through three named mounts, lights it, and scrubs the resulting cue marks. Raw URLs stay inside the source drawer. A corrected caption track may be mounted once; the contract re-fetches the original transcript and standard, rejects either if its digest changed, and preserves that the visible result came from the patch round.

## Call sheet

```text
mount_reel -> OPEN
light_reel -> AUDITED / READY|REPAIR|BLOCKED
mount_patch (owner, once) -> PATCHED / READY|REPAIR|BLOCKED
```

Validators retrieve every source themselves. `READY` is impossible when coverage is below 95, any cue index remains, or any issue code is present. Demo files are operator-created fixtures, not independent authorities.

## Rehearse locally

```text
genvm-lint lint contracts/contract.py
python -m pytest -q
node --check site/app.js
```

The reviewed contract is deployed on StudioNet at [`0x90507eB04c75D79378eEFA95b7B4e530e74f5d03`](https://explorer-studio.genlayer.com/address/0x90507eB04c75D79378eEFA95b7B4e530e74f5d03). Its finalized deployment receipt is recorded in `deployment.json`; lifecycle transactions and canonical readback are recorded in `evidence/live-run.json` after the live rehearsal. The earlier `0xFe9d…9235` rehearsal deployment is retired and is not used by the interface.
