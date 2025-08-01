# Bitcoin Price Predictor

Real-time Bitcoin price prediction application with live market data and ML-powered forecasting.

## 🚀 Live Demo

**[https://btcpricepredictor.vibe8.app](https://btcpricepredictor.vibe8.app)**

## Business Applications

### Financial Trading Platforms
- **Real-time price feeds** for cryptocurrency exchanges
- **Algorithmic trading signals** for automated systems
- **Risk management tools** with predictive analytics
- **Market making strategies** using order book data

### Investment Management
- **Portfolio optimization** with price forecasting
- **Risk assessment** for cryptocurrency investments
- **Market timing** for institutional trades
- **Performance analytics** for fund managers

### Enterprise Integration
- **API-first architecture** for easy integration
- **Scalable microservices** for high-volume trading
- **Real-time data streaming** for trading applications
- **Production-ready infrastructure** with Docker deployment

## Technology Stack

**Backend:** Go (high-performance APIs) + Python (ML predictions)
**Frontend:** JavaScript + CSS
**Data:** Real-time Coinbase Pro WebSocket feeds
**Deployment:** Docker containers

## Key Features

- **Real-time Bitcoin prices** from Coinbase Pro
- **ML-powered predictions** with 5-minute forecasts
- **Live order book data** showing market depth
- **Professional trading interface** with responsive design
- **High-performance APIs** built with Go
- **Production-ready architecture** with Docker deployment

## Quick Start

### Docker Deployment
```bash
git clone https://github.com/jimhouserock/BitcoinPricePredictor_Python_Golang.git
cd BitcoinPricePredictor_Python_Golang
docker-compose up -d
```

### Local Development
```bash
cd go-service
go mod tidy
go run main.go
```

Access at: http://localhost:3000

## API Endpoints

- `GET /` - Web interface
- `GET /price` - Current Bitcoin price
- `GET /predict` - ML price prediction
- `GET /orderbook` - Live order book data
- `GET /health` - Service health status

---

**Built by [Vibe8.app](https://vibe8.app)** - Modern full-stack development with Go APIs and Python data science.
