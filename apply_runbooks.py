import pandas as pd
import yaml
import os

# Load telemetry
df = pd.read_csv('../logs/predictions.csv')

# Load runbooks
runbook_files = ['../runbooks/reroute.yml', '../runbooks/qos_adjust.yml', '../runbooks/rate_limit.yml']

for rb_file in runbook_files:
    with open(rb_file) as f:
        rb = yaml.safe_load(f)
        for _, row in df.iterrows():
            apply = False
            for cond, expr in rb['conditions'].items():
                val = row[cond]
                if eval(f"{val}{expr}"):
                    apply = True
            if apply:
                for act in rb['actions']:
                    if 'command' in act:
                        print(f"Executing: {act['command'].format(**row)}")
                    if 'log' in act:
                        with open('../logs/runbook_log.txt', 'a') as logf:
                            logf.write(act['log'].format(**row)+'\n')
