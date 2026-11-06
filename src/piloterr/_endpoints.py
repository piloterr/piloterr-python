"""Generated from the Piloterr OpenAPI document. Do not edit by hand."""

from __future__ import annotations

from .models import EndpointDefinition

ENDPOINTS: dict[str, EndpointDefinition] = {
    "aboutyou_product": EndpointDefinition(
        path="/v2/aboutyou/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "aboutyou_search": EndpointDefinition(
        path="/v2/aboutyou/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "action_product": EndpointDefinition(
        path="/v2/action/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "action_search": EndpointDefinition(
        path="/v2/action/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "aldi_product": EndpointDefinition(
        path="/v2/aldi/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "aldi_search": EndpointDefinition(
        path="/v2/aldi/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "alibaba_product": EndpointDefinition(
        path="/v2/alibaba/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "alibaba_search": EndpointDefinition(
        path="/v2/alibaba/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "aliexpress_product": EndpointDefinition(
        path="/v2/aliexpress/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "aliexpress_product_reviews": EndpointDefinition(
        path="/v2/aliexpress/product/reviews",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "aliexpress_search": EndpointDefinition(
        path="/v2/aliexpress/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "aliexpress_store_product": EndpointDefinition(
        path="/v2/aliexpress/store/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "allegro_product": EndpointDefinition(
        path="/v2/allegro/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "allegro_search": EndpointDefinition(
        path="/v2/allegro/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "amazon_product": EndpointDefinition(
        path="/v2/amazon/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "amazon_product_offer": EndpointDefinition(
        path="/v2/amazon/product/offer",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "amazon_search": EndpointDefinition(
        path="/v2/amazon/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "apartments_property": EndpointDefinition(
        path="/v2/apartments/property",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "apartments_search": EndpointDefinition(
        path="/v2/apartments/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "argenprop_property": EndpointDefinition(
        path="/v2/argenprop/property",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "argenprop_search": EndpointDefinition(
        path="/v2/argenprop/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "argos_product": EndpointDefinition(
        path="/v2/argos/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "argos_search": EndpointDefinition(
        path="/v2/argos/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "arxiv_paper": EndpointDefinition(
        path="/v2/arxiv/paper",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "arxiv_search": EndpointDefinition(
        path="/v2/arxiv/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "auchan_product": EndpointDefinition(
        path="/v2/auchan/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "auchan_search": EndpointDefinition(
        path="/v2/auchan/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "autodoc_product": EndpointDefinition(
        path="/v2/autodoc/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "autodoc_product_related": EndpointDefinition(
        path="/v2/autodoc/product/related",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(
            "query",
            "maker_id",
            "vehicle_type",
            "maker_name",
            "product_id",
        ),
    ),
    "autodoc_search": EndpointDefinition(
        path="/v2/autodoc/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "autoeurope_result": EndpointDefinition(
        path="/v2/autoeurope/result",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(
            "offer_id",
            "pickup",
            "pickup_date",
            "dropoff_date",
        ),
    ),
    "autoeurope_search": EndpointDefinition(
        path="/v2/autoeurope/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(
            "pickup",
            "pickup_date",
            "dropoff_date",
        ),
    ),
    "autoscout24_ad": EndpointDefinition(
        path="/v2/autoscout24/ad",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "autoscout24_search": EndpointDefinition(
        path="/v2/autoscout24/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "autotrader_ad": EndpointDefinition(
        path="/v2/autotrader/ad",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "autotrader_search": EndpointDefinition(
        path="/v2/autotrader/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "bestbuy_product": EndpointDefinition(
        path="/v2/bestbuy/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "bestbuy_product_reviews": EndpointDefinition(
        path="/v2/bestbuy/product/reviews",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "bestbuy_search": EndpointDefinition(
        path="/v2/bestbuy/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "bhphotovideo_product": EndpointDefinition(
        path="/v2/bhphotovideo/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "bhphotovideo_search": EndpointDefinition(
        path="/v2/bhphotovideo/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "bing_search": EndpointDefinition(
        path="/v2/bing/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "bitiba_product": EndpointDefinition(
        path="/v2/bitiba/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "bitiba_search": EndpointDefinition(
        path="/v2/bitiba/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "bol_product": EndpointDefinition(
        path="/v2/bol/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "bol_search": EndpointDefinition(
        path="/v2/bol/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "boulanger_product": EndpointDefinition(
        path="/v2/boulanger/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "boulanger_search": EndpointDefinition(
        path="/v2/boulanger/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "brave_search": EndpointDefinition(
        path="/v2/brave/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "bricodepot_product": EndpointDefinition(
        path="/v2/bricodepot/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "bricodepot_search": EndpointDefinition(
        path="/v2/bricodepot/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "bricorama_product": EndpointDefinition(
        path="/v2/bricorama/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "bricorama_search": EndpointDefinition(
        path="/v2/bricorama/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "carrefour_product": EndpointDefinition(
        path="/v2/carrefour/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "carrefour_search": EndpointDefinition(
        path="/v2/carrefour/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "carrefour_suggest": EndpointDefinition(
        path="/v2/carrefour/suggest",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "castorama_product": EndpointDefinition(
        path="/v2/castorama/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "castorama_search": EndpointDefinition(
        path="/v2/castorama/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "cdiscount_product": EndpointDefinition(
        path="/v2/cdiscount/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "cdiscount_product_offer": EndpointDefinition(
        path="/v2/cdiscount/product/offer",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "cdiscount_search": EndpointDefinition(
        path="/v2/cdiscount/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "centris_property": EndpointDefinition(
        path="/v2/centris/property",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "centris_search": EndpointDefinition(
        path="/v2/centris/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "chewy_product": EndpointDefinition(
        path="/v2/chewy/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "chewy_search": EndpointDefinition(
        path="/v2/chewy/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "clearedjobs_job": EndpointDefinition(
        path="/v2/clearedjobs/job",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "clearedjobs_search": EndpointDefinition(
        path="/v2/clearedjobs/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "company": EndpointDefinition(
        path="/v2/company",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "coolblue_product": EndpointDefinition(
        path="/v2/coolblue/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "coolblue_search": EndpointDefinition(
        path="/v2/coolblue/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "copart_lot": EndpointDefinition(
        path="/v2/copart/lot",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "copart_search": EndpointDefinition(
        path="/v2/copart/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "costco_product": EndpointDefinition(
        path="/v2/costco/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "costco_search": EndpointDefinition(
        path="/v2/costco/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "crunchbase_company_info": EndpointDefinition(
        path="/v2/crunchbase/company/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(),
    ),
    "crunchbase_event": EndpointDefinition(
        path="/v2/crunchbase/event",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "crunchbase_funding_round": EndpointDefinition(
        path="/v2/crunchbase/funding_round",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "crunchbase_funding_rounds": EndpointDefinition(
        path="/v2/crunchbase/funding_rounds",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(),
    ),
    "crunchbase_people_info": EndpointDefinition(
        path="/v2/crunchbase/people/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "crunchbase_search": EndpointDefinition(
        path="/v2/crunchbase/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "cultura_product": EndpointDefinition(
        path="/v2/cultura/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "cultura_search": EndpointDefinition(
        path="/v2/cultura/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "darty_product": EndpointDefinition(
        path="/v2/darty/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "darty_search": EndpointDefinition(
        path="/v2/darty/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "datasets_linkedin_company": EndpointDefinition(
        path="/v2/datasets/linkedin/company",
        methods=("POST",),
        response="json",
        required=(),
    ),
    "decathlon_product": EndpointDefinition(
        path="/v2/decathlon/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "decathlon_search": EndpointDefinition(
        path="/v2/decathlon/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "digikey_product": EndpointDefinition(
        path="/v2/digikey/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "digikey_search": EndpointDefinition(
        path="/v2/digikey/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "doaj_article": EndpointDefinition(
        path="/v2/doaj/article",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "doaj_journal": EndpointDefinition(
        path="/v2/doaj/journal",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "doaj_search": EndpointDefinition(
        path="/v2/doaj/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "domain_dnsbl": EndpointDefinition(
        path="/v2/domain/dnsbl",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "domain_malicious": EndpointDefinition(
        path="/v2/domain/malicious",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "domain_whois": EndpointDefinition(
        path="/v2/domain/whois",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "domaincomau_property": EndpointDefinition(
        path="/v2/domaincomau/property",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "domaincomau_search": EndpointDefinition(
        path="/v2/domaincomau/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "duckduckgo_search": EndpointDefinition(
        path="/v2/duckduckgo/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "ebay_product": EndpointDefinition(
        path="/v2/ebay/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "ebay_search": EndpointDefinition(
        path="/v2/ebay/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "elcorteingles_product": EndpointDefinition(
        path="/v2/elcorteingles/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "elcorteingles_search": EndpointDefinition(
        path="/v2/elcorteingles/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "eleclerc_product": EndpointDefinition(
        path="/v2/eleclerc/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "eleclerc_search": EndpointDefinition(
        path="/v2/eleclerc/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "eleclerc_suggest": EndpointDefinition(
        path="/v2/eleclerc/suggest",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "email_analyzes": EndpointDefinition(
        path="/v2/email/analyzes",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "email_finder": EndpointDefinition(
        path="/v2/email/finder",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "email_verify": EndpointDefinition(
        path="/v2/email/verify",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "europages_company": EndpointDefinition(
        path="/v2/europages/company",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "europages_search": EndpointDefinition(
        path="/v2/europages/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "eventbrite_event": EndpointDefinition(
        path="/v2/eventbrite/event",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "eventbrite_search": EndpointDefinition(
        path="/v2/eventbrite/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(),
    ),
    "expedia_ad": EndpointDefinition(
        path="/v2/expedia/ad",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "expedia_flight": EndpointDefinition(
        path="/v2/expedia/flight",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "expedia_search": EndpointDefinition(
        path="/v2/expedia/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "fashionphile_product": EndpointDefinition(
        path="/v2/fashionphile/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "fashionphile_search": EndpointDefinition(
        path="/v2/fashionphile/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "finder_chewy_products": EndpointDefinition(
        path="/v2/finder/chewy-products",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(),
    ),
    "finder_eleclerc_stores": EndpointDefinition(
        path="/v2/finder/eleclerc-stores",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "finder_google_countries": EndpointDefinition(
        path="/v2/finder/google-countries",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "finder_google_languages": EndpointDefinition(
        path="/v2/finder/google-languages",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "finder_google_locations": EndpointDefinition(
        path="/v2/finder/google-locations",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "finder_leroymerlin_products": EndpointDefinition(
        path="/v2/finder/leroymerlin-products",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(),
    ),
    "finder_leroymerlin_stores": EndpointDefinition(
        path="/v2/finder/leroymerlin-stores",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "finder_linkedin_industries": EndpointDefinition(
        path="/v2/finder/linkedin-industries",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "finder_mrbricolage_stores": EndpointDefinition(
        path="/v2/finder/mrbricolage-stores",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "fiverr_profile_info": EndpointDefinition(
        path="/v2/fiverr/profile/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "fiverr_search": EndpointDefinition(
        path="/v2/fiverr/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "fnac_product": EndpointDefinition(
        path="/v2/fnac/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "fnac_search": EndpointDefinition(
        path="/v2/fnac/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "fotocasa_ad": EndpointDefinition(
        path="/v2/fotocasa/ad",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "fotocasa_search": EndpointDefinition(
        path="/v2/fotocasa/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "franchisedirect_franchise": EndpointDefinition(
        path="/v2/franchisedirect/franchise",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "franchisedirect_search": EndpointDefinition(
        path="/v2/franchisedirect/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "fressnapf_product": EndpointDefinition(
        path="/v2/fressnapf/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "fressnapf_search": EndpointDefinition(
        path="/v2/fressnapf/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "funda_property": EndpointDefinition(
        path="/v2/funda/property",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "funda_search": EndpointDefinition(
        path="/v2/funda/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "g2_product_info": EndpointDefinition(
        path="/v2/g2/product/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "github_user_info": EndpointDefinition(
        path="/v2/github/user/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "glassdoor_company_info": EndpointDefinition(
        path="/v2/glassdoor/company/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "glassdoor_company_search": EndpointDefinition(
        path="/v2/glassdoor/company/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "glassdoor_job_info": EndpointDefinition(
        path="/v2/glassdoor/job/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "glassdoor_job_search": EndpointDefinition(
        path="/v2/glassdoor/job/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "goodreads_book": EndpointDefinition(
        path="/v2/goodreads/book",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "goodreads_search": EndpointDefinition(
        path="/v2/goodreads/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "google_images": EndpointDefinition(
        path="/v2/google/images",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "google_jobs": EndpointDefinition(
        path="/v2/google/jobs",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "google_maps": EndpointDefinition(
        path="/v2/google/maps",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "google_news": EndpointDefinition(
        path="/v2/google/news",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "google_search": EndpointDefinition(
        path="/v2/google/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "google_search_ai": EndpointDefinition(
        path="/v2/google/search/ai",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "google_search_autocomplete": EndpointDefinition(
        path="/v2/google/search/autocomplete",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "google_shopping": EndpointDefinition(
        path="/v2/google/shopping",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "google_videos": EndpointDefinition(
        path="/v2/google/videos",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "googleadstransparency_ad": EndpointDefinition(
        path="/v2/googleadstransparency/ad",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "googleadstransparency_search": EndpointDefinition(
        path="/v2/googleadstransparency/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "grainger_product": EndpointDefinition(
        path="/v2/grainger/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "grainger_search": EndpointDefinition(
        path="/v2/grainger/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "greenhouse_job": EndpointDefinition(
        path="/v2/greenhouse/job",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "greenhouse_search": EndpointDefinition(
        path="/v2/greenhouse/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "gsaelibrary_contract": EndpointDefinition(
        path="/v2/gsaelibrary/contract",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "gsaelibrary_search": EndpointDefinition(
        path="/v2/gsaelibrary/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "homestra_ad": EndpointDefinition(
        path="/v2/homestra/ad",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "homestra_search": EndpointDefinition(
        path="/v2/homestra/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "huggingface_model": EndpointDefinition(
        path="/v2/huggingface/model",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "huggingface_search": EndpointDefinition(
        path="/v2/huggingface/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "idealista_property": EndpointDefinition(
        path="/v2/idealista/property",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "idealista_provinces": EndpointDefinition(
        path="/v2/idealista/provinces",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(),
    ),
    "idealista_search": EndpointDefinition(
        path="/v2/idealista/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "idealo_product": EndpointDefinition(
        path="/v2/idealo/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "idealo_search": EndpointDefinition(
        path="/v2/idealo/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "ikea_product": EndpointDefinition(
        path="/v2/ikea/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "ikea_search": EndpointDefinition(
        path="/v2/ikea/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "immobilienscout24_property": EndpointDefinition(
        path="/v2/immobilienscout24/property",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "immobilienscout24_search": EndpointDefinition(
        path="/v2/immobilienscout24/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "immoscout24ch_search": EndpointDefinition(
        path="/v2/immoscout24ch/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "immowelt_property": EndpointDefinition(
        path="/v2/immowelt/property",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "immowelt_search": EndpointDefinition(
        path="/v2/immowelt/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "imoveisweb_property": EndpointDefinition(
        path="/v2/imoveisweb/property",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "imoveisweb_search": EndpointDefinition(
        path="/v2/imoveisweb/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "indeed_company_info": EndpointDefinition(
        path="/v2/indeed/company/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "indeed_company_search": EndpointDefinition(
        path="/v2/indeed/company/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "indeed_job_info": EndpointDefinition(
        path="/v2/indeed/job/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "indeed_job_salary": EndpointDefinition(
        path="/v2/indeed/job/salary",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "indeed_job_search": EndpointDefinition(
        path="/v2/indeed/job/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "inet_product": EndpointDefinition(
        path="/v2/inet/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "inet_search": EndpointDefinition(
        path="/v2/inet/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "instagram_post_info": EndpointDefinition(
        path="/v2/instagram/post/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "instagram_user_info": EndpointDefinition(
        path="/v2/instagram/user/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "intermarche_product": EndpointDefinition(
        path="/v2/intermarche/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(
            "query",
            "shop_id",
        ),
    ),
    "intermarche_search": EndpointDefinition(
        path="/v2/intermarche/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(
            "query",
            "shop_id",
        ),
    ),
    "intersport_product": EndpointDefinition(
        path="/v2/intersport/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "intersport_search": EndpointDefinition(
        path="/v2/intersport/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "jamesedition_property": EndpointDefinition(
        path="/v2/jamesedition/property",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "jamesedition_search": EndpointDefinition(
        path="/v2/jamesedition/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "jobs": EndpointDefinition(
        path="/v1/jobs/{id}",
        methods=("GET",),
        response="json",
        required=("id",),
    ),
    "kick_user_info": EndpointDefinition(
        path="/v2/kick/user/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "kijiji_ad": EndpointDefinition(
        path="/v2/kijiji/ad",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "kijiji_search": EndpointDefinition(
        path="/v2/kijiji/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "kroger_product": EndpointDefinition(
        path="/v2/kroger/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "kroger_search": EndpointDefinition(
        path="/v2/kroger/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "lamudi_ad": EndpointDefinition(
        path="/v2/lamudi/ad",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "lamudi_search": EndpointDefinition(
        path="/v2/lamudi/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(),
    ),
    "leboncoin_ad": EndpointDefinition(
        path="/v2/leboncoin/ad",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "leboncoin_search": EndpointDefinition(
        path="/v2/leboncoin/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "leboncoin_search_api": EndpointDefinition(
        path="/v2/leboncoin/search_api",
        methods=("POST",),
        response="json",
        required=(),
    ),
    "lenovo_product": EndpointDefinition(
        path="/v2/lenovo/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "lenovo_search": EndpointDefinition(
        path="/v2/lenovo/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "leroymerlin_product": EndpointDefinition(
        path="/v2/leroymerlin/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "leroymerlin_search": EndpointDefinition(
        path="/v2/leroymerlin/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "lidl_product": EndpointDefinition(
        path="/v2/lidl/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "lidl_search": EndpointDefinition(
        path="/v2/lidl/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "linkedin_company_info": EndpointDefinition(
        path="/v2/linkedin/company/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(),
    ),
    "linkedin_job_count": EndpointDefinition(
        path="/v2/linkedin/job/count",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(),
    ),
    "linkedin_job_info": EndpointDefinition(
        path="/v2/linkedin/job/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "linkedin_job_search": EndpointDefinition(
        path="/v2/linkedin/job/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(),
    ),
    "linkedin_job_suggest": EndpointDefinition(
        path="/v2/linkedin/job/suggest",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "linkedin_post_info": EndpointDefinition(
        path="/v2/linkedin/post/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "linkedin_product_info": EndpointDefinition(
        path="/v2/linkedin/product/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "linkedin_profile_info": EndpointDefinition(
        path="/v2/linkedin/profile/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "linkedinadlibrary_ad": EndpointDefinition(
        path="/v2/linkedinadlibrary/ad",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "linkedinadlibrary_search": EndpointDefinition(
        path="/v2/linkedinadlibrary/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(),
    ),
    "loopnet_property": EndpointDefinition(
        path="/v2/loopnet/property",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "loopnet_search": EndpointDefinition(
        path="/v2/loopnet/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "maersk_tracking": EndpointDefinition(
        path="/v2/maersk/tracking",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "manomano_product": EndpointDefinition(
        path="/v2/manomano/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "manomano_product_offer": EndpointDefinition(
        path="/v2/manomano/product/offer",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "manomano_search": EndpointDefinition(
        path="/v2/manomano/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "mascus_ad": EndpointDefinition(
        path="/v2/mascus/ad",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "mascus_search": EndpointDefinition(
        path="/v2/mascus/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "mediamarkt_product": EndpointDefinition(
        path="/v2/mediamarkt/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "mediamarkt_search": EndpointDefinition(
        path="/v2/mediamarkt/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "micromania_product": EndpointDefinition(
        path="/v2/micromania/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "micromania_search": EndpointDefinition(
        path="/v2/micromania/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "mobile_ad": EndpointDefinition(
        path="/v2/mobile/ad",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "mobile_search": EndpointDefinition(
        path="/v2/mobile/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "morele_product": EndpointDefinition(
        path="/v2/morele/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "morele_search": EndpointDefinition(
        path="/v2/morele/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "mrbricolage_suggest": EndpointDefinition(
        path="/v2/mrbricolage/suggest",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "newegg_product": EndpointDefinition(
        path="/v2/newegg/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "newegg_search": EndpointDefinition(
        path="/v2/newegg/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "northdata_company": EndpointDefinition(
        path="/v2/northdata/company",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "northdata_search": EndpointDefinition(
        path="/v2/northdata/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "npi_provider": EndpointDefinition(
        path="/v2/npi/provider",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "npi_search": EndpointDefinition(
        path="/v2/npi/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(),
    ),
    "oceanio_search": EndpointDefinition(
        path="/v2/oceanio/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "olx_ad": EndpointDefinition(
        path="/v2/olx/ad",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "olx_product": EndpointDefinition(
        path="/v2/olx/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "olx_search": EndpointDefinition(
        path="/v2/olx/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "oscaro_product": EndpointDefinition(
        path="/v2/oscaro/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "oscaro_search": EndpointDefinition(
        path="/v2/oscaro/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "ovoko_ad": EndpointDefinition(
        path="/v2/ovoko/ad",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "ovoko_search": EndpointDefinition(
        path="/v2/ovoko/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "owler_company_info": EndpointDefinition(
        path="/v2/owler/company/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "owler_search": EndpointDefinition(
        path="/v2/owler/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "pagesjaunes_page_info": EndpointDefinition(
        path="/v2/pagesjaunes/page/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "pagesjaunes_search": EndpointDefinition(
        path="/v2/pagesjaunes/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "patreon_profile_info": EndpointDefinition(
        path="/v2/patreon/profile/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "patreon_search": EndpointDefinition(
        path="/v2/patreon/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "petsmart_product": EndpointDefinition(
        path="/v2/petsmart/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "petsmart_search": EndpointDefinition(
        path="/v2/petsmart/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "picard_product": EndpointDefinition(
        path="/v2/picard/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "picard_search": EndpointDefinition(
        path="/v2/picard/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "pinterest_user_info": EndpointDefinition(
        path="/v2/pinterest/user/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "pitchbook_company_info": EndpointDefinition(
        path="/v2/pitchbook/company/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "pitchbook_search": EndpointDefinition(
        path="/v2/pitchbook/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "pointp_product": EndpointDefinition(
        path="/v2/pointp/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "pointp_search": EndpointDefinition(
        path="/v2/pointp/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "prnewswire_article": EndpointDefinition(
        path="/v2/prnewswire/article",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "prnewswire_search": EndpointDefinition(
        path="/v2/prnewswire/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "producthunt_product_info": EndpointDefinition(
        path="/v2/producthunt/product/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "proshop_product": EndpointDefinition(
        path="/v2/proshop/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "proshop_search": EndpointDefinition(
        path="/v2/proshop/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "rappi_product": EndpointDefinition(
        path="/v2/rappi/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "rappi_search": EndpointDefinition(
        path="/v2/rappi/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "ratemyprofessors_professor": EndpointDefinition(
        path="/v2/ratemyprofessors/professor",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "ratemyprofessors_search": EndpointDefinition(
        path="/v2/ratemyprofessors/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "realestatecomau_search": EndpointDefinition(
        path="/v2/realestatecomau/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "realtor_property": EndpointDefinition(
        path="/v2/realtor/property",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "realtor_search": EndpointDefinition(
        path="/v2/realtor/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "redfin_property": EndpointDefinition(
        path="/v2/redfin/property",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "redfin_search": EndpointDefinition(
        path="/v2/redfin/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "reichelt_product": EndpointDefinition(
        path="/v2/reichelt/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "reichelt_search": EndpointDefinition(
        path="/v2/reichelt/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "reverb_product": EndpointDefinition(
        path="/v2/reverb/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "reverb_search": EndpointDefinition(
        path="/v2/reverb/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "rexel_product": EndpointDefinition(
        path="/v2/rexel/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "rexel_search": EndpointDefinition(
        path="/v2/rexel/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "rightmove_property": EndpointDefinition(
        path="/v2/rightmove/property",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "rightmove_search": EndpointDefinition(
        path="/v2/rightmove/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "rsonline_product": EndpointDefinition(
        path="/v2/rsonline/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "rsonline_search": EndpointDefinition(
        path="/v2/rsonline/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "seek_job": EndpointDefinition(
        path="/v2/seek/job",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "seek_search": EndpointDefinition(
        path="/v2/seek/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "seloger_agency": EndpointDefinition(
        path="/v2/seloger/agency",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "seloger_agency_rent": EndpointDefinition(
        path="/v2/seloger/agency/rent",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "seloger_agency_sale": EndpointDefinition(
        path="/v2/seloger/agency/sale",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "seloger_property": EndpointDefinition(
        path="/v2/seloger/property",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "seloger_search": EndpointDefinition(
        path="/v2/seloger/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "sephora_product": EndpointDefinition(
        path="/v2/sephora/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "sephora_search": EndpointDefinition(
        path="/v2/sephora/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "shophouzz_product": EndpointDefinition(
        path="/v2/shophouzz/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "shopify_apps": EndpointDefinition(
        path="/v2/shopify/apps",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "shopify_catalog": EndpointDefinition(
        path="/v2/shopify/catalog",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "shopify_collections": EndpointDefinition(
        path="/v2/shopify/collections",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "shopify_product": EndpointDefinition(
        path="/v2/shopify/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "similarweb_domain": EndpointDefinition(
        path="/v2/similarweb/domain",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "similarweb_search": EndpointDefinition(
        path="/v2/similarweb/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "snapeda_product": EndpointDefinition(
        path="/v2/snapeda/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "snapeda_search": EndpointDefinition(
        path="/v2/snapeda/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "starbucks_menu": EndpointDefinition(
        path="/v2/starbucks/menu",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(),
    ),
    "starbucks_product": EndpointDefinition(
        path="/v2/starbucks/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "starbucks_search": EndpointDefinition(
        path="/v2/starbucks/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(),
    ),
    "stats": EndpointDefinition(
        path="/v2/stats",
        methods=("GET",),
        response="json",
        required=(),
    ),
    "stockx_product": EndpointDefinition(
        path="/v2/stockx/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "stockx_search": EndpointDefinition(
        path="/v2/stockx/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "stockx_trends": EndpointDefinition(
        path="/v2/stockx/trends",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "stubhub_event": EndpointDefinition(
        path="/v2/stubhub/event",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "stubhub_search": EndpointDefinition(
        path="/v2/stubhub/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "target_product": EndpointDefinition(
        path="/v2/target/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "target_search": EndpointDefinition(
        path="/v2/target/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "tdlr_license": EndpointDefinition(
        path="/v2/tdlr/license",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "tdlr_search": EndpointDefinition(
        path="/v2/tdlr/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(),
    ),
    "ted_notice": EndpointDefinition(
        path="/v2/ted/notice",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "ted_search": EndpointDefinition(
        path="/v2/ted/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(),
    ),
    "thalia_product": EndpointDefinition(
        path="/v2/thalia/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "thalia_search": EndpointDefinition(
        path="/v2/thalia/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "thefork_restaurant": EndpointDefinition(
        path="/v2/thefork/restaurant",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "thefork_search": EndpointDefinition(
        path="/v2/thefork/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "thomasnet_company": EndpointDefinition(
        path="/v2/thomasnet/company",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "thomasnet_search": EndpointDefinition(
        path="/v2/thomasnet/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "ticketmaster_event": EndpointDefinition(
        path="/v2/ticketmaster/event",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "ticketmaster_search": EndpointDefinition(
        path="/v2/ticketmaster/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "tiktoktopads_ad": EndpointDefinition(
        path="/v2/tiktoktopads/ad",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "tiktoktopads_search": EndpointDefinition(
        path="/v2/tiktoktopads/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(),
    ),
    "tradeaplane_listing": EndpointDefinition(
        path="/v2/tradeaplane/listing",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "tradeaplane_search": EndpointDefinition(
        path="/v2/tradeaplane/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "trustpilot_company_info": EndpointDefinition(
        path="/v2/trustpilot/company/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "untappd_beer": EndpointDefinition(
        path="/v2/untappd/beer",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "untappd_search": EndpointDefinition(
        path="/v2/untappd/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "upwork_freelancer": EndpointDefinition(
        path="/v2/upwork/freelancer",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "upwork_jobs": EndpointDefinition(
        path="/v2/upwork/jobs",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "upwork_services": EndpointDefinition(
        path="/v2/upwork/services",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "upwork_services_info": EndpointDefinition(
        path="/v2/upwork/services/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "usage": EndpointDefinition(
        path="/v2/usage",
        methods=("GET",),
        response="json",
        required=(),
    ),
    "usaspending_award": EndpointDefinition(
        path="/v2/usaspending/award",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "usaspending_search": EndpointDefinition(
        path="/v2/usaspending/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "vestiairecollective_product": EndpointDefinition(
        path="/v2/vestiairecollective/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "vestiairecollective_search": EndpointDefinition(
        path="/v2/vestiairecollective/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "vinted_item": EndpointDefinition(
        path="/v2/vinted/item",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "vinted_search": EndpointDefinition(
        path="/v2/vinted/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "vinted_user_info": EndpointDefinition(
        path="/v2/vinted/user/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "vivareal_property": EndpointDefinition(
        path="/v2/vivareal/property",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "vivareal_search": EndpointDefinition(
        path="/v2/vivareal/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "walmart_product": EndpointDefinition(
        path="/v2/walmart/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "walmart_search": EndpointDefinition(
        path="/v2/walmart/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "walmart_suggest": EndpointDefinition(
        path="/v2/walmart/suggest",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "website_antibot": EndpointDefinition(
        path="/v2/website/antibot",
        methods=("GET",),
        response="json",
        required=("query",),
    ),
    "website_crawler": EndpointDefinition(
        path="/v2/website/crawler",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "website_email_phone_extractor": EndpointDefinition(
        path="/v2/website/email_phone_extractor",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "website_rendering": EndpointDefinition(
        path="/v2/website/rendering",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "website_screenshot": EndpointDefinition(
        path="/v2/website/screenshot",
        methods=(
            "GET",
            "POST",
        ),
        response="any",
        required=("url",),
    ),
    "website_technology": EndpointDefinition(
        path="/v2/website/technology",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "website_webunlocker": EndpointDefinition(
        path="/v2/website/webunlocker",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "weibo_post_info": EndpointDefinition(
        path="/v2/weibo/post/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "weibo_search": EndpointDefinition(
        path="/v2/weibo/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "welcometothejungle_company": EndpointDefinition(
        path="/v2/welcometothejungle/company",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "welcometothejungle_search": EndpointDefinition(
        path="/v2/welcometothejungle/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "wellfound_company_info": EndpointDefinition(
        path="/v2/wellfound/company/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "x_post_info": EndpointDefinition(
        path="/v2/x/post/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "x_profile_info": EndpointDefinition(
        path="/v2/x/profile/info",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "yahoo_search": EndpointDefinition(
        path="/v2/yahoo/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "yellowpages_business": EndpointDefinition(
        path="/v2/yellowpages/business",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "yellowpages_search": EndpointDefinition(
        path="/v2/yellowpages/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "yelp_business": EndpointDefinition(
        path="/v2/yelp/business",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "yelp_reviews": EndpointDefinition(
        path="/v2/yelp/reviews",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "yelp_search": EndpointDefinition(
        path="/v2/yelp/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "zapimoveis_ad": EndpointDefinition(
        path="/v2/zapimoveis/ad",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "zapimoveis_search": EndpointDefinition(
        path="/v2/zapimoveis/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "zazzle_product": EndpointDefinition(
        path="/v2/zazzle/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "zazzle_search": EndpointDefinition(
        path="/v2/zazzle/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "zillow_property": EndpointDefinition(
        path="/v2/zillow/property",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "zillow_search": EndpointDefinition(
        path="/v2/zillow/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "zonaprop_property": EndpointDefinition(
        path="/v2/zonaprop/property",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "zonaprop_search": EndpointDefinition(
        path="/v2/zonaprop/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "zoopla_property": EndpointDefinition(
        path="/v2/zoopla/property",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "zoopla_search": EndpointDefinition(
        path="/v2/zoopla/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "zooplus_product": EndpointDefinition(
        path="/v2/zooplus/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "zooplus_search": EndpointDefinition(
        path="/v2/zooplus/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "zoro_product": EndpointDefinition(
        path="/v2/zoro/product",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "zoro_search": EndpointDefinition(
        path="/v2/zoro/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
}
