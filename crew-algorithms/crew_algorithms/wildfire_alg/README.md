# CREW-WILDFIRE

[![license badge](https://img.shields.io/badge/license-Apache--2.0-green.svg)](LICENSE)

CREW-WILDFIRE is an open-source benchmark designed to evaluate LLM-based multi-agent Agentic AI systems in complex, dynamic, real-world tasks. Built atop the human-AI teaming CREW simulation platform, it provides procedurally generated wildfire response scenarios that test the limits of multi-agent coordination, communication, and planning under uncertainty.

## Overview

CREW-WILDFIRE addresses the gap in existing multi-agent benchmarks by offering:

- Large-scale environments supporting 100+ agents
- Heterogeneous agent types (drones, helicopters, bulldozers, firefighters)
- Partial observability and stochastic dynamics
- Long-horizon planning objectives
- Both low-level control and high-level natural language interactions
- Modular PERCEPTION and EXECUTION interfaces

Through these features, researchers can evaluate and develop next-generation multi-agent Agentic AI frameworks in realistic disaster response scenarios.

## Implemented Algorithms

CREW-WILDFIRE includes implementations of four state-of-the-art LLM-based multi-agent frameworks:

* **CAMON**: A hybrid coordination system featuring dynamic leadership where task assignments and global updates are managed by a leader agent. Leadership roles can transfer through agent-initiated interactions, enabling flexible communication and delegation.

* **COELA**: A fully decentralized framework where agents independently propose information, evaluate communication necessity, and execute actions based on their generated plans.

* **Embodied**: A decentralized system without leader agents, featuring alternating communication rounds that allow both broadcast and targeted message exchanges, followed by independent action planning.

* **HMAS-2**: A hybrid framework combining centralized planning with distributed agent feedback. The system proposes actions through a central planner and refines them through agent consensus.

These implementations showcase different approaches to multi-agent coordination, from fully decentralized to hybrid architectures, enabling comprehensive evaluation of various coordination strategies.

## Key Features

* **Procedural Environment Generation**: Dynamic creation of environments using Perlin noise textures for vegetation, elevation, moisture, settlement, and wind vector maps
* **Heterogeneous Agent Support**: Multiple agent types with diverse capabilities
* **Scalable Architecture**: Support for large-scale agent deployment (100+ agents)
* **Flexible Interaction Modes**: Both low-level control primitives and natural language commands
* **Comprehensive Evaluation**: Built-in metrics for assessing coordination, spatial reasoning, and plan adaptation
* **LLM Integration**: Native support for implementing and testing LLM-based multi-agent frameworks
* **Real-world Complexity**: Partial observability, stochastic dynamics, and complex objectives

## Project Structure

```
.
├── algorithms/           # Main algorithm implementations
│   ├── coela/           # COELA algorithm implementation
│   ├── embodied_agents/ # Embodied agents implementation
│   ├── hmas_2/         # HMAS 2.0 implementation
│   ├── manual/         # Manual control implementation
│   └── template/       # Template for new algorithms
│
├── libraries/           # Action and option libraries
│   ├── *_action_library.py  # Action definitions for different agents
│   └── *_option_library.py  # Option definitions for different agents
│
├── core/               # Core functionality
│   ├── alg_utils.py   # Common algorithm utilities
│   └── utils.py       # General utility functions
│
├── config/            # Configuration management
│   ├── build_config.py # Configuration builder
│   └── configs.py     # Configuration definitions
│
├── data/             # Data scripts
│
└── outputs/          # All output files
    ├── logs/         # All chat logs, scores, and screenshots
    ├── plots/        # Generated plots
    └── data/         # Output data files
```

## Contributing

CREW-WILDFIRE is designed to accelerate progress in large-scale Agentic intelligence. We welcome contributions that:

1. Implement new LLM-based multi-agent frameworks
2. Add novel evaluation metrics or scenarios
3. Improve environment generation or simulation features
4. Enhance documentation and examples
5. Fix bugs or improve performance

Please follow these steps to contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Coding Standards

- Follow PEP 8 guidelines
- Include docstrings for all functions and classes
- Add unit tests for new features
- Update documentation as needed

## License

[PENDING LICENSE SELECTION]

## Citation

If you use CREW-WILDFIRE in your research, please cite our paper:

[CITATION DETAILS PENDING]

```bibtex
@inproceedings{crew-wildfire2025,
    title={CREW-WILDFIRE: A Benchmark for Large-Scale Multi-Agent Agentic AI in Disaster Response},
    author={[Author Names]},
    booktitle={39th Conference on Neural Information Processing Systems (NeurIPS 2025)},
    year={2025}
}
``` 