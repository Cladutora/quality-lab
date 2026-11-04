# Master's project: Python LSTM model for Bitcoin analysis

## Problem and research context

Explore how historical cryptocurrency data can support predictive modelling, and compare models developed in Python and R. This was academic research, not a deployed trading product.

**Dissertation:** Oportunidades de Inversión en Criptomonedas: Análisis Predictivo y Estrategias Basadas en Big Data.

**Team authors listed in the dissertation:** Clarissa Solino, Sergio Romero, Sebastián Fernández and José Barroso.

## My contribution

I developed the Python model using a recurrent neural network with LSTM layers. I began with tutorial/reference code and adapted it through iterative changes to the data source, indicators, network configuration and training settings. The dissertation describes the development and compares the Python approach with the team's R models.

My Python project is also published in my own repository:

[View the Python model](https://github.com/Cladutora/masters-python-lstm/blob/main/src/bitcoin_lstm.py)

## Technical workflow

1. Retrieve historical BTC/USDT market data through ccxt and Binance.
2. Prepare data and scale numerical inputs.
3. Build sequential input windows for the recurrent model.
4. Configure and train TensorFlow/Keras LSTM layers.
5. Generate predictions and compare them with observed values.
6. Examine tabular outputs and charts to understand model behaviour.

## What this demonstrates for QA and AI roles

- Practical Python work with external data and numerical libraries.
- Investigation of dependencies, data preparation and model behaviour.
- Iterative experimentation and comparison of expected versus observed results.
- Documentation of methods and findings within a shared research project.

## Reproducibility and validation status

The historical project has not been rerun in the current environment. This portfolio does not claim a fresh successful training run or a production accuracy score. A reusable dependency specification and independent reproduction are follow-up work. My Python code is hosted separately with provenance linking back to the original team repository. The team's R models and dissertation are not copied.

## Limitations

The project is evidence of Python and modelling work, not evidence of reliable future market returns. Historical predictive results do not establish real-world trading performance. No financial-return or model-accuracy percentage is claimed here without a reproducible evaluation definition.
