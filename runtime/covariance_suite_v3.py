import json,math,hashlib,pathlib,platform
# encounter-plane isotropic Gaussian screening proxy; explicit non-operational scope
miss=9.790430764895484;sigma=20.;hard_body=5.
# small-area approximation around miss point: Pc ~= area * 2D Gaussian density at miss
pc=(hard_body**2/(2*sigma**2))*math.exp(-(miss**2)/(2*sigma**2));ok=0<pc<1
out={"farm":130,"engine":"python-ssa-covariance-suite-v3","test":"ISOTROPIC_ENCOUNTER_PLANE_PC_PROXY","miss_distance_m":miss,"sigma_m":sigma,"hard_body_radius_m":hard_body,"collision_probability_proxy":pc,"status":"COVARIANCE_PROXY_OK" if ok else "FAIL","scope":"SCREENING_PROXY_NOT_OPERATIONAL_PC_NOT_CDM_VALIDATION","python":platform.python_version()};raw=json.dumps(out,sort_keys=True).encode();out["result_sha256"]=hashlib.sha256(raw).hexdigest();pathlib.Path("artifacts").mkdir(exist_ok=True);pathlib.Path("artifacts/f130_covariance_suite_v3.json").write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out));raise SystemExit(0 if ok else 1)
