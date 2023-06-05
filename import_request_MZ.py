import requests

import json

import time

import pandas as pd

# Defina as credenciais de acesso à API
base_url = 'https://ssr86921.live.dynatrace.com/api/config/v1' # Substitua <seu-tenant> pelo seu tenant no Dynatrace
api_token = 'dt0c01.NTWYMGRO6CFSB7Y44QMQBZY5.OA7A5P5JDVYTOHOGTCTH6YDV2R4R43INQPBNETP6ACWPUCHYLX2XT7C6Q4QHZAC6'  # Substitua <seu-api-token> pelo seu token de acesso à API

# Define o cabeçalho da solicitação com o token de acesso à API
headers = {
    'Authorization': 'Api-Token ' + api_token,
    'Content-Type': 'application/json'
}

# Carrega os dados da planilha Excel usando a biblioteca pandas
df = pd.read_excel('autotag_insert.xlsx')  # Substitua 'caminho-para-planilha.xlsx' pelo caminho correto da sua planilha


# Itera sobre as linhas da planilha
for row in df.itertuples():
    managementZones_id = str(row.id)
    ambiente_value = str(row.aplicacao)

       
    new_managementZones= {
        "id": managementZones_id,
        "name": "SGC.PLARD." + ambiente_value + ".PCI.QA" + str(),
        "description": ambiente_value,
        "rules": [
            {
            "type": "CUSTOM_DEVICE",
            "enabled": True,
            "propagationTypes": [],
            "conditions": [
                {
                "key": {
                    "attribute": "CUSTOM_DEVICE_NAME",
                    "type": "STATIC"
                },
                "comparisonInfo": {
                    "type": "STRING",
                    "operator": "BEGINS_WITH",
                    "value": "SGC.PLARD." + ambiente_value + ".PCI.QA",
                    "negate": False,
                    "caseSensitive": True
                }
                }
            ]
            },
            {
            "type": "HOST",
            "enabled": True,
            "propagationTypes": [
                "HOST_TO_PROCESS_GROUP_INSTANCE"
            ],
            "conditions": [
                {
                "key": {
                    "attribute": "HOST_GROUP_NAME",
                    "type": "STATIC"
                },
                "comparisonInfo": {
                    "type": "STRING",
                    "operator": "EQUALS",
                    "value": "SGC.PLARD." + ambiente_value + ".PCI.QA",
                    "negate": False,
                    "caseSensitive": False
                }
                }
            ]
            },
            {
            "type": "AWS_RELATIONAL_DATABASE_SERVICE",
            "enabled": True,
            "propagationTypes": [],
            "conditions": [
                {
                "key": {
                    "attribute": "AWS_RELATIONAL_DATABASE_SERVICE_TAGS",
                    "type": "STATIC"
                },
                "comparisonInfo": {
                    "type": "TAG",
                    "operator": "EQUALS",
                    "value": {
                    "context": "AWS",
                    "key": "env",
                    "value": "qa"
                    },
                    "negate": False
                }
                },
                {
                "key": {
                    "attribute": "AWS_RELATIONAL_DATABASE_SERVICE_NAME",
                    "type": "STATIC"
                },
                "comparisonInfo": {
                    "type": "STRING",
                    "operator": "CONTAINS",
                    "value": "-pci-",
                    "negate": False,
                    "caseSensitive": False
                }
                },
                {
                "key": {
                    "attribute": "AWS_RELATIONAL_DATABASE_SERVICE_ENDPOINT",
                    "type": "STATIC"
                },
                "comparisonInfo": {
                    "type": "STRING",
                    "operator": "CONTAINS",
                    "value":  ambiente_value,
                    "negate": False,
                    "caseSensitive": False
                }
                }
            ]
            },
            {
            "type": "PROCESS_GROUP",
            "enabled": True,
            "propagationTypes": [
                "PROCESS_GROUP_TO_HOST",
                "PROCESS_GROUP_TO_SERVICE"
            ],
            "conditions": [
                {
                "key": {
                    "attribute": "KUBERNETES_CLUSTER_NAME",
                    "type": "STATIC"
                },
                "comparisonInfo": {
                    "type": "STRING",
                    "operator": "EQUALS",
                    "value": "pci-eks-qa",
                    "negate": False,
                    "caseSensitive": False
                }
                },
                {
                "key": {
                    "attribute": "CLOUD_APPLICATION_NAMESPACE_NAME",
                    "type": "STATIC"
                },
                "comparisonInfo": {
                    "type": "STRING",
                    "operator": "EQUALS",
                    "value": ambiente_value,
                    "negate": False,
                    "caseSensitive": False
                }
                }
            ]
            },
            {
            "type": "CLOUD_APPLICATION_NAMESPACE",
            "enabled": True,
            "propagationTypes": [],
            "conditions": [
                {
                "key": {
                    "attribute": "KUBERNETES_CLUSTER_NAME",
                    "type": "STATIC"
                },
                "comparisonInfo": {
                    "type": "STRING",
                    "operator": "EQUALS",
                    "value": "pci-eks-qa",
                    "negate": False,
                    "caseSensitive": False
                }
                },
                {
                "key": {
                    "attribute": "CLOUD_APPLICATION_NAMESPACE_NAME",
                    "type": "STATIC"
                },
                "comparisonInfo": {
                    "type": "STRING",
                    "operator": "EQUALS",
                    "value": ambiente_value,
                    "negate": False,
                    "caseSensitive": False
                }
                }
            ]
            },
            {
            "type": "KUBERNETES_SERVICE",
            "enabled": True,
            "propagationTypes": [],
            "conditions": [
                {
                "key": {
                    "attribute": "KUBERNETES_CLUSTER_NAME",
                    "type": "STATIC"
                },
                "comparisonInfo": {
                    "type": "STRING",
                    "operator": "EQUALS",
                    "value": "pci-eks-qa",
                    "negate": False,
                    "caseSensitive": False
                }
                },
                {
                "key": {
                    "attribute": "CLOUD_APPLICATION_NAMESPACE_NAME",
                    "type": "STATIC"
                },
                "comparisonInfo": {
                    "type": "STRING",
                    "operator": "EQUALS",
                    "value": ambiente_value,
                    "negate": False,
                    "caseSensitive": False
                }
                }
            ]
            },
            {
            "type": "CLOUD_APPLICATION",
            "enabled": True,
            "propagationTypes": [],
            "conditions": [
                {
                "key": {
                    "attribute": "KUBERNETES_CLUSTER_NAME",
                    "type": "STATIC"
                },
                "comparisonInfo": {
                    "type": "STRING",
                    "operator": "EQUALS",
                    "value": "pci-eks-qa",
                    "negate": False,
                    "caseSensitive": False
                }
                },
                {
                "key": {
                    "attribute": "CLOUD_APPLICATION_NAMESPACE_NAME",
                    "type": "STATIC"
                },
                "comparisonInfo": {
                    "type": "STRING",
                    "operator": "EQUALS",
                    "value": ambiente_value,
                    "negate": False,
                    "caseSensitive": False
                }
                }
            ]
            },
            {
            "type": "SERVICE",
            "enabled": True,
            "propagationTypes": [
                "SERVICE_TO_HOST_LIKE",
                "SERVICE_TO_PROCESS_GROUP_LIKE"
            ],
            "conditions": [
                {
                "key": {
                    "attribute": "AWS_RELATIONAL_DATABASE_SERVICE_ENDPOINT",
                    "type": "STATIC"
                },
                "comparisonInfo": {
                    "type": "STRING",
                    "operator": "CONTAINS",
                    "value": "pci",
                    "negate": False,
                    "caseSensitive": True
                }
                },
                {
                "key": {
                    "attribute": "AWS_RELATIONAL_DATABASE_SERVICE_TAGS",
                    "type": "STATIC"
                },
                "comparisonInfo": {
                    "type": "TAG",
                    "operator": "EQUALS",
                    "value": {
                        "context": "AWS",
                        "key": "env",
                        "value": "qa"
                    },
                    "negate": False
                }                  
            },
                {
                "key": {
                    "attribute": "AWS_RELATIONAL_DATABASE_SERVICE_ENDPOINT",
                    "type": "STATIC"
                },
                "comparisonInfo": {
                    "type": "STRING",
                    "operator": "CONTAINS",
                    "value": ambiente_value,
                    "negate": False,
                    "caseSensitive": False
                }
                }
            ]
            }
        ],
        "dimensionalRules": [],
        "entitySelectorBasedRules": []
 }


    # Faz a chamada para a API para atualizar o autoTag
    response = requests.put(base_url + '/managementZones/'+ managementZones_id, headers=headers, data=json.dumps(new_managementZones))
    print(response)

    # Verifica se a chamada foi bem-sucedida (código de resposta 204)
    if response.status_code == 204:
        print('O autoTag foi atualizado com sucesso para o valor:', ambiente_value)
    else:
        print('Falha na chamada à API para o valor:', ambiente_value)

    # Verifica se a chamada foi bem-sucedida (código de resposta 204)
    if response.status_code == 204:
        print('O autoTag foi atualizado com sucesso para o ID:', managementZones_id)
    else:
        print('Falha na chamada à API para o ID:', managementZones_id)

    time.sleep(2)

    print(response.text)
