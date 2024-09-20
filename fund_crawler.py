import os
import json
from crawl4ai.chunking_strategy import *
from crawl4ai.extraction_strategy import *
from crawl4ai.crawler_strategy import *
from crawl4ai.web_crawler import WebCrawler
from pydantic import BaseModel, Field



class FundData(BaseModel):
    fund_name: str = Field(..., description="Name of the fund.")
    fund_code: str = Field (..., description = "Code of the fund.")
    asset_class: str = Field(..., description= "Asset Class of the fund.")
    apr: Optional[float] = Field(None, description="Annual Percentage Rate.")
    sharpe_ratio: Optional[float] = Field(None, description="Sharpe Ratio of the fund.")
    max_drawdown: Optional[float] = Field(None, description="Drawdown percentage.")
    inception_date: Optional[str] = Field(None, description="Inception date of the fund.")
    beta: Optional[float] = Field(None, description = "Beta of the fund")
    summary: Optional[str] = Field(None, description="Detailed summary of the fund.")
    portfolio_managers: List[str] = Field([], description="List of portfolio managers.")
    keywords: List[str] = Field([], description="List of keywords associated with the fund.")
    


class FundCrawler:
    def __init__(self):
        self.crawler = WebCrawler()
        self.crawler.warmup()
        api_key = os.getenv('API_KEY')
        if not api_key:
            raise ValueError("API_KEY environment variable not set.")
        self.api_key = api_key

    def extract_fund_data(self, url):
        result = self.crawler.run(
            url=url,
            word_count_threshold=1,
            extraction_strategy= LLMExtractionStrategy(
                provider= "openai/gpt-4o-mini", api_token = self.api_key,
                schema=FundData.model_json_schema(),
                extraction_type="schema",
                apply_chunking =False,
                instruction="From the crawled content visit all the fund links on the page for actual fund performance, extract the following details: "\
                    "1. Fund Name"\
                    "2. APR"\
                    "3. Sharpe Ratio"\
                    "4. Max Drawdown"\
                    "5. Inception Date"\
                    "6. Summary"\
                    "7. Portfolio Manager of the fund, Just the name no accreditation"\
                    "8. Asset Class of the fund, Equity, Credit etc."\
                    "9. Fund Code"\
                    'The extracted JSON format should look like this: '\
                    '{ "fund_name": "Fund Name", "summary": "Detailed summary of the page.", "brief_summary": "Brief summary in a paragraph." }'
            ),
            bypass_cache=True,
        )

        page_summary = json.loads(result.extracted_content)
        return page_summary 