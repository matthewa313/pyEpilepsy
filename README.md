# pyEpilepsy

A Python module for EEG feature extraction to aid in epileptic episode (seizure) prediction.

## Disclaimer

I am building a device that can predict epileptic episodes from brain waves using machine learning. This python module is being built to aide in live-time feature extraction of brain wave data and has been optimized specifically for my device. I have open sourced via GitHub for no reason other than convenience.  The functions contained within the module are NOT general purpose functions and must be largely adapted for other use. Also, much of this code was developed by taking existing code from forestboa/pyEEG and scipy/scipy and optimizing it for my needs.

## Getting Started

These instructions will get you using these feature extraction functions in your machine learning pipeline or signal processing algorithms.

### Prerequisites

```
numpy >= 1.9.2
```

### Installing via Pip

Through the command line:

```
pip install git+https://github.com/matthewa313/pyEpilepsy.git
```

## Contributing

This an open-sourced Python container for a private-source machine learning project. If you are interested in contributing, send me an email at manderson63@cherrycreekschools.org

## Versioning

I am not currently versioning.

## Authors

* **Matthew Anderson** - *Package Author* - [matthewa313](https://github.com/matthewa313)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Much code is taken from Forest Bao's infinitely better pyEEG package.
