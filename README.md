# Aggrid Custom Grid Streamlit API Enablement

A Streamlit custom component that provides customizable grids with API integration.

## Features

- Customizable grid options
- API integration for data handling
- Pagination, sorting, and filtering
- Modern UI with themes

## Installation

```bash
pip install streamlit-custom-api-grid
```

## Demo
see a demo of the grid in action at quantqueen.com/LiveBot 


## Usage

```python
from custom_grid import st_custom_grid, GridOptionsBuilder, JsCode

gb = GridOptionsBuilder.create()
gb.configure_grid_options(pagination=True, 
                            paginationPageSize=100, 
                        #   suppressPaginationPanel=True, 
                            enableRangeSelection=True, 
                            copyHeadersToClipboard=True,
                            sideBar=True,
                            sortable=True
                        ) 
gb.configure_default_column(column_width=100, 
                            resizable=True, 
                            wrapText=False, 
                            wrapHeaderText=True, 
                            sortable=True, 
                            autoHeaderHeight=True, 
                            autoHeight=True, 
                            suppress_menu=False, 
                            filter=True, 
                            minWidth=89,
                            cellStyle={"fontSize": "15px"})            
gb.configure_index('symbol')
gb.configure_theme('ag-theme-material')
go = gb.build()
            st_custom_grid(
                key=f'key',
                client_user=client_user, # optional used for api 
                username=client_user, # optional used for api  
                api=f"{ip_address}/api/data/story",
                # api_ws=f"{ip_address}/api/data/ws_story", # use Websocket to handle data change
                api_update=f"{ip_address}/api/data/update_queenking_chessboard", # used for api secondary api plug option
                refresh_sec=refresh_sec, # how long grid awaits before calling to refresh data (use NONE for buttons)
                refresh_cutoff_sec=seconds_to_market_close, # timer for when to stop auto refreshing from refresh_sec
                prod=st.session_state['prod'], # optional used for api  
                grid_options=go,
                return_type='story', # optional used for api  
                # kwargs from here
                api_lastmod_key=f"REVREC", # optional used for api  
                prompt_message = "symbol", # optional used for api  
                prompt_field = "symbol", # optional used for api  
                api_key=os.environ.get("fastAPI_key"), # optional used for api  
                symbols=symbols, # optional used for api  
                buttons=g_buttons, # optional used for api  
                grid_height='550px',
                toggle_views = toggle_views, # optional
                allow_unsafe_jscode=True,
                columnOrder=story_col_order, # optional arrange columns
                refresh_success=True,
                total_col="symbol", # where total is located
                subtotal_cols = [], 
                filter_apply=True, # filters on grid
                filter_button='piece_name', # filters on grid speific columns for fast filters buttons
                show_clear_all_filters=True,
                column_sets ={},
#                 column_sets = {
#     "Simple View": ["col1", "col2"],
#     "Options Trader": ["col3", "col4"],
#   }, # used to arrange columns

        )
```
```

## Development

This project consists of:
- Python backend using Streamlit
- React/TypeScript frontend

### Requirements

- Python >= 3.7
- Streamlit >= 1.0.0
- Node.js (for frontend development)

## License

MIT License

## Author

Stefan Stapinski

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

