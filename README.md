# Pytorch Benchmarks

This script benchmarks various deep learning models using different batch sizes on the ImageNet dataset. The script downloads images from the ImageNet dataset, processes them using specified models, and reports accuracy and time taken for each batch size.

## Prerequisites

- Python 3.8
- PyTorch 1.12.0
- `torchvision` 0.13.0
- `requests`
- `tqdm`
- `memory_profiler`
- `PIL` (Pillow)
- Access to Hugging Face Datasets API

## Getting Started

1. Clone the repository or download the script `benchmarks.py`.

2. Install the required dependencies using `pip`:

   ```bash
   pip install torch==1.12.0 torchvision==0.13.0 requests tqdm pillow memory_profiler
   ```
3. Set up your Hugging Face API token as an environment variable named HF_API_TOKEN.
4. Run the benchmarks script using the provided shell script:
   ```bash
   ./run_benchmarks.sh
   ```
   The run_benchmarks.sh script will execute benchmarks for all models and batch sizes specified within the script.
5. The script will execute benchmarks for each model and batch size combination, saving results to a CSV file named `report.csv`.

## File Descriptions
- `benchmarks.py`: The main script for performing benchmarks.
- `run_benchmarks.sh`: Shell script to automate running benchmarks with different parameters.
- `images/`: A directory to store downloaded images.
- `report.csv`: A CSV file containing benchmark results.

## Notes
- The script uses pretrained models from torchvision and performs inference on the ImageNet validation set.
- The `HF_API_TOKEN` environment variable is required to access the Hugging Face Datasets API.
