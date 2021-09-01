print('Initializing')

from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from azure.devops.v5_1.release.models import BuildVersion, ArtifactMetadata, ReleaseStartMetadata
from gpiozero import LED, Button
from signal import pause
import pprint
import time

# Fill in with your personal access token and org URL
personal_access_token = 'ilykq7ypqmledu64xxrthio6cja4anmtiihx4iobf54xqprpdlga'
organization_url = 'https://dev.azure.com/revlocal'
projectName = 'GitRepos'
projectDefinitionId = 140

# Assign pins to our LEDS
blueLed = LED(4)
greenLed = LED(17)
button = Button(2)

# Device is on so we turn green
blueLed.on()

def createRelease():
    print("Button was pressed")

    # Device is running release so we turn blue
    blueLed.off()
    greenLed.blink()

    # Create a connection to the org
    print('Create connection...')
    credentials = BasicAuthentication('', personal_access_token)
    connection = Connection(base_url=organization_url, creds=credentials)

    # Instantiate  release client
    release_client = connection.clients.get_release_client()

    #projectDefinition = release_client.get_release_definition(project=projectName, definition_id=projectDefinitionId)
    #print(projectDefinition)

    # Create base metadata with project id of release
    rsm = ReleaseStartMetadata(definition_id=projectDefinitionId, is_draft=False, artifacts=None)
    print('Create Release...')
    response = release_client.create_release(release_start_metadata=rsm, project=projectName)
    print(response)

    # Device triggered build now we wait
    greenLed.off()
    blueLed.on()

while True:
    if button.is_pressed:
        createRelease()
    else:
        print('Waiting for button press')
