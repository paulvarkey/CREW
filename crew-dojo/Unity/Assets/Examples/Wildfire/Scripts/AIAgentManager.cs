using System;
using System.Linq;
using System.Collections.Generic;
using UnityEngine;
using Unity.MLAgents;
using Unity.MLAgents.SideChannels;
using Unity.MLAgents.Sensors;
using Dojo;
using Unity.Netcode;


namespace Examples.Wildfire
{
    public class AIAgentManager : MonoBehaviour
    {
        [SerializeField]
        public GameObject _firefighterAgentPrefab;
        public GameObject _bulldozerAgentPrefab;
        public GameObject _droneAgentPrefab;
        public GameObject _helicopterAgentPrefab;
        public GameObject _managerAgentPrefab;
        public GameObject _defaultAgentPrefab;


        private DojoConnection _connection;
        private GameManager _gameManager;
        private EventChannel _eventChannel
;
        public List<AIAgent> Agents = new();
        public Queue<AIAgent> UnusedAgents = new();
        

        public int NumAgents;
        public int StartingFirefighterAgents;
        public int StartingBulldozerAgents;
        public int StartingDroneAgents;
        public int StartingHelicopterAgents;
        public int AgentIndex;


        private void Awake()
        {


            _connection = FindObjectOfType<DojoConnection>();
            _gameManager = FindObjectOfType<GameManager>();
            NumAgents = 0;
            StartingFirefighterAgents = 0;
            StartingBulldozerAgents = 0;
            StartingDroneAgents = 0;
            StartingHelicopterAgents = 0;
            AgentIndex = 0;




            var args = Environment.GetCommandLineArgs();

            Debug.Log(args);
            for (var idx = 0; idx < args.Length; ++idx)
            {
                var arg = args[idx];

                if (arg.Equals("-NumAgents") && idx < args.Length - 1 && int.TryParse(args[idx + 1], out var num) && num >= 0)
                {
                    NumAgents = num;
                    
                    Debug.Log("recieved max agents: " + NumAgents);

                }
                else if (arg.Equals("-StartingFirefighterAgents") && idx < args.Length - 1 && int.TryParse(args[idx + 1], out var firenum) && firenum >= 0)
                {
                    StartingFirefighterAgents = firenum;
                    
                    Debug.Log("recieved starting firefighter agents: " + StartingFirefighterAgents);
                }
                else if (arg.Equals("-StartingBulldozerAgents") && idx < args.Length - 1 && int.TryParse(args[idx + 1], out var bullnum) && bullnum >= 0)
                {
                    StartingBulldozerAgents = bullnum;

                    Debug.Log("recieved starting bulldozer agents: " + StartingBulldozerAgents);
                }
                else if (arg.Equals("-StartingDroneAgents") && idx < args.Length - 1 && int.TryParse(args[idx + 1], out var dronenum) && dronenum >= 0)
                {
                    StartingDroneAgents = dronenum;

                    Debug.Log("recieved starting drone agents: " + StartingDroneAgents);
                }
                else if (arg.Equals("-StartingHelicopterAgents") && idx < args.Length - 1 && int.TryParse(args[idx + 1], out var helinum) && helinum >= 0)
                {
                    StartingHelicopterAgents = helinum;

                    Debug.Log("recieved starting helicopter agents: " + StartingHelicopterAgents);
                }

            }
            if (NumAgents == 0)
            {
                NumAgents = 100;
            }

            //StartingFirefighterAgents =10;
            //StartingBulldozerAgents = 5;
            //StartingDroneAgents = 10;
            //StartingHelicopterAgents = 5;



        }




        public void SpawnAgents(Vector2 spawn_location)
        {
            
            List<String> players = new List<string>();


            for (int i = 0; i < NumAgents; i++) {

 

                GameObject gameAgent = Instantiate(_defaultAgentPrefab, new Vector3(0,-100,0), Quaternion.identity);
                AIAgent agent = gameAgent.GetComponent<AIAgent>();


                agent.AgentId = -1;
                UnusedAgents.Enqueue(agent);
                agent.ResetAgent();

            }

            Vector2 spawn_location_game = new Vector2(spawn_location.x - (ConfigReader.map_size / 2), -spawn_location.y + (ConfigReader.map_size / 2));
            
            RaycastHit hit;

            Physics.Raycast(new Vector3(spawn_location_game.x, 0, spawn_location_game.y) + new Vector3(0f, 1000f, 0f), new Vector3(0, -1, 0), out hit);
            float height = 1000- hit.distance;
           

            SpawnAgent(ControllerType.Manager, new Vector3(spawn_location_game.x, height+0.1f, spawn_location_game.y));
            for(int i = 0; i < StartingFirefighterAgents; i++)
            {
                SpawnAgent(ControllerType.Firefighter, new Vector3(spawn_location_game.x, height + 0.2f, spawn_location_game.y));
            }
            for (int i = 0; i < StartingBulldozerAgents; i++)
            {
                SpawnAgent(ControllerType.Bulldozer, new Vector3(spawn_location_game.x, height + 10f, spawn_location_game.y));
            }
            for (int i = 0; i < StartingDroneAgents; i++)
            {
                SpawnAgent(ControllerType.Drone, new Vector3(spawn_location_game.x, height + 25f, spawn_location_game.y));
            }
            for (int i = 0; i < StartingHelicopterAgents; i++)
            {

                SpawnAgent(ControllerType.Helicopter, new Vector3(spawn_location_game.x, 10, spawn_location_game.y));
            }

           

        }
        public void SpawnAgent(ControllerType type, Vector3 pos)
        {
            if (!_connection.IsServer)
                throw new NotServerException("You must spawn agents on the server for server ownership");


            List<String> players = new List<string>();
            players.Add("Agent-" + AgentIndex.ToString() + "");
            AgentIndex = _connection.RegisterAIPlayers(players);
            

            var prefab = this.gameObject;
            switch (type) {
                case ControllerType.Firefighter:
                    prefab = _firefighterAgentPrefab;
                    break;
                case ControllerType.Bulldozer:
                    prefab = _bulldozerAgentPrefab;
                    break;
                case ControllerType.Drone:
                    prefab = _droneAgentPrefab;
                    break;
                case ControllerType.Helicopter:
                    prefab = _helicopterAgentPrefab;
                    break;
                case ControllerType.Manager:
                    prefab = _managerAgentPrefab;
                    break;
            }


            AIAgent agent = UnusedAgents.Dequeue();
            agent.controllerType = type;

            

            GameObject controller = Instantiate(prefab, new Vector3(pos.x, pos.y, pos.z), Quaternion.identity);
            PlayerController c = controller.GetComponent<PlayerController>();
            NetworkObject netObj = controller.GetComponent<NetworkObject>();
            agent.transform.SetParent(c.transform);


            agent.controller = c;
            c.agent = agent;
            agent.AgentId = AgentIndex - 1;
            Agents.Add(agent);
            agent.ResetAgent();
            netObj.Spawn();


            


        }


        private void Initialize()
        {
            Debug.Assert(_connection.IsServer);

            if (Academy.IsInitialized)
            {
                // register MLAgent environment
                _eventChannel = new(_connection);
                if (_eventChannel.IsInitialized)
                {
                    SideChannelManager.RegisterSideChannel(_eventChannel);
                }
            }
        }

        private void OnDestroy()
        {
            if (Academy.IsInitialized)
            {
                if (_eventChannel.IsInitialized)
                {
                    SideChannelManager.UnregisterSideChannel(_eventChannel);
                }
            }
        }

    }

}