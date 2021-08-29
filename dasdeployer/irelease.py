from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from gpiozero import LEDBoard, ButtonBoard, Button
import pprint

# Fill in with your personal access token and org URL
personal_access_token = 'nope'
organization_url = 'https://dev.azure.com/revlocal'
projectDefinitionId = 140

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

release_client = connection.clients.get_release_client()
#releaseStartMetadata = ReleaseStartMetadata(definition_id=projectDefinitionId)
#print(releaseStartMetadata)
projectDefinition = release_client.get_release_definition(project='GitRepos', definition_id=projectDefinitionId)
print(projectDefinition)

statusLed = LEDBoard(red=4, pwm=True)
statusLed.on()
sleep(3)
statusLed.off()

