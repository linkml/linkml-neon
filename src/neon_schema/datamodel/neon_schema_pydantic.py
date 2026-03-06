/Users/athessen/linkml-neon/.venv/lib/python3.12/site-packages/requests/__init__.py:113: RequestsDependencyWarning: urllib3 (2.6.3) or chardet (7.0.1)/charset_normalizer (3.4.5) doesn't match a supported version!
  warnings.warn(
from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.7.0"
version = "0.1.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'neon',
     'default_range': 'string',
     'description': 'LinkML schema for National Ecological Observatory Network '
                    "(NEON) data. This schema models NEON's hierarchical data "
                    'structure including domains, sites, locations, data products, '
                    'samples, and taxonomic information with cross-links between '
                    'entities.',
     'id': 'https://w3id.org/neon-schema',
     'imports': ['linkml:types'],
     'license': 'MIT',
     'name': 'neon_schema',
     'prefixes': {'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'dwc': {'prefix_prefix': 'dwc',
                          'prefix_reference': 'http://rs.tdwg.org/dwc/terms/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'neon': {'prefix_prefix': 'neon',
                           'prefix_reference': 'https://w3id.org/neon-schema/'},
                  'orcid': {'prefix_prefix': 'orcid',
                            'prefix_reference': 'https://orcid.org/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'wgs84': {'prefix_prefix': 'wgs84',
                            'prefix_reference': 'http://www.w3.org/2003/01/geo/wgs84_pos#'}},
     'source_file': 'src/neon_schema/schema/neon_schema.yaml',
     'title': 'NEON Data Schema',
     'types': {'DomainCode': {'description': 'Domain code in format D01-D20',
                              'from_schema': 'https://w3id.org/neon-schema',
                              'name': 'DomainCode',
                              'pattern': '^D[0-2][0-9]$',
                              'typeof': 'string'},
               'ProductCode': {'description': 'Data product code in format '
                                              'DPX.XXXXX.XXX',
                               'from_schema': 'https://w3id.org/neon-schema',
                               'name': 'ProductCode',
                               'pattern': '^DP[0-4]\\.[0-9]{5}\\.[0-9]{3}$',
                               'typeof': 'string'},
               'SiteCode': {'description': 'Four-character site code',
                            'from_schema': 'https://w3id.org/neon-schema',
                            'name': 'SiteCode',
                            'pattern': '^[A-Z]{4}$',
                            'typeof': 'string'},
               'YearMonth': {'description': 'Year-month in YYYY-MM format',
                             'from_schema': 'https://w3id.org/neon-schema',
                             'name': 'YearMonth',
                             'pattern': '^[0-9]{4}-[0-1][0-9]$',
                             'typeof': 'string'}}} )

class SiteTypeEnum(str, Enum):
    """
    Type of NEON field site
    """
    CORE = "CORE"
    """
    Core sites selected to represent key ecosystem types
    """
    GRADIENT = "GRADIENT"
    """
    Gradient sites capturing environmental gradients
    """


class ProductStatusEnum(str, Enum):
    """
    Status of a data product
    """
    FUTURE = "FUTURE"
    """
    Product planned for future release
    """
    ACTIVE = "ACTIVE"
    """
    Product currently being collected and released
    """
    RETIRED = "RETIRED"
    """
    Product no longer being collected
    """


class ProductCategoryEnum(str, Enum):
    """
    Data product processing level
    """
    Level_0 = "Level 0"
    """
    Raw data
    """
    Level_1 = "Level 1"
    """
    Quality-controlled data
    """
    Level_2 = "Level 2"
    """
    Derived data products
    """
    Level_3 = "Level 3"
    """
    Highly processed/modeled data
    """
    Level_4 = "Level 4"
    """
    Integrated data products
    """


class TaxonTypeEnum(str, Enum):
    """
    Major taxonomic groupings used by NEON
    """
    ALGAE = "ALGAE"
    """
    Algae taxa
    """
    BEETLE = "BEETLE"
    """
    Beetle taxa (Carabidae)
    """
    BIRD = "BIRD"
    """
    Bird taxa
    """
    FISH = "FISH"
    """
    Fish taxa
    """
    HERPETOLOGY = "HERPETOLOGY"
    """
    Reptile and amphibian taxa
    """
    MACROINVERTEBRATE = "MACROINVERTEBRATE"
    """
    Aquatic macroinvertebrate taxa
    """
    MOSQUITO = "MOSQUITO"
    """
    Mosquito taxa
    """
    MOSQUITO_PATHOGENS = "MOSQUITO_PATHOGENS"
    """
    Mosquito pathogen taxa
    """
    PLANT = "PLANT"
    """
    Plant taxa
    """
    SMALL_MAMMAL = "SMALL_MAMMAL"
    """
    Small mammal taxa
    """
    TICK = "TICK"
    """
    Tick taxa
    """


class LocationTypeEnum(str, Enum):
    """
    Types of named locations in NEON hierarchy
    """
    REALM = "REALM"
    """
    Top-level realm
    """
    DOMAIN = "DOMAIN"
    """
    Ecological domain
    """
    SITE = "SITE"
    """
    Field site
    """
    TOWER = "TOWER"
    """
    Instrumented tower
    """
    PLOT = "PLOT"
    """
    Sampling plot
    """
    POINT = "POINT"
    """
    Observation point
    """
    SENSOR = "SENSOR"
    """
    Individual sensor location
    """


class MeasurementSystemEnum(str, Enum):
    """
    NEON measurement system types
    """
    AOP = "AOP"
    """
    Airborne Observation Platform
    """
    AIS = "AIS"
    """
    Aquatic Instrument System
    """
    AOS = "AOS"
    """
    Aquatic Observation System
    """
    TIS = "TIS"
    """
    Terrestrial Instrument System
    """
    TOS = "TOS"
    """
    Terrestrial Observation System
    """



class NeonDataset(ConfiguredBaseModel):
    """
    Container for a collection of NEON data entities
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/neon-schema', 'tree_root': True})

    domains: Optional[list[Domain]] = Field(default=None, description="""Collection of NEON domains""", json_schema_extra = { "linkml_meta": {'domain_of': ['NeonDataset']} })
    sites: Optional[list[Site]] = Field(default=None, description="""Collection of NEON field sites""", json_schema_extra = { "linkml_meta": {'domain_of': ['NeonDataset', 'Domain', 'DataProduct']} })
    locations: Optional[list[Location]] = Field(default=None, description="""Collection of named locations""", json_schema_extra = { "linkml_meta": {'domain_of': ['NeonDataset', 'Site']} })
    data_products: Optional[list[DataProduct]] = Field(default=None, description="""Collection of data products""", json_schema_extra = { "linkml_meta": {'domain_of': ['NeonDataset', 'Release', 'BiorepositoryCollection']} })
    releases: Optional[list[Release]] = Field(default=None, description="""Collection of data releases""", json_schema_extra = { "linkml_meta": {'domain_of': ['NeonDataset', 'DataProduct']} })
    taxa: Optional[list[Taxon]] = Field(default=None, description="""Collection of taxonomic records""", json_schema_extra = { "linkml_meta": {'domain_of': ['NeonDataset']} })
    samples: Optional[list[Sample]] = Field(default=None, description="""Collection of physical samples""", json_schema_extra = { "linkml_meta": {'domain_of': ['NeonDataset', 'BiorepositoryCollection']} })


class Domain(ConfiguredBaseModel):
    """
    A NEON domain representing a distinct eco-climatic region. NEON divides the US into 20 eco-climatic domains.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Place', 'from_schema': 'https://w3id.org/neon-schema'})

    domain_code: str = Field(default=..., description="""Unique domain identifier (D01-D20)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Domain'], 'slot_uri': 'dcterms:identifier'} })
    domain_name: str = Field(default=..., description="""Full name of the domain""", json_schema_extra = { "linkml_meta": {'domain_of': ['Domain'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Description of the domain's ecological characteristics""", json_schema_extra = { "linkml_meta": {'domain_of': ['Domain', 'Release'], 'slot_uri': 'schema:description'} })
    sites: Optional[list[str]] = Field(default=None, description="""Sites within this domain""", json_schema_extra = { "linkml_meta": {'domain_of': ['NeonDataset', 'Domain', 'DataProduct']} })


class Site(ConfiguredBaseModel):
    """
    A NEON field site where data collection occurs. Sites are either CORE (representing key ecosystems) or GRADIENT (capturing environmental gradients).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Place', 'from_schema': 'https://w3id.org/neon-schema'})

    site_code: str = Field(default=..., description="""Four-character unique site identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Site'], 'slot_uri': 'dcterms:identifier'} })
    site_name: str = Field(default=..., description="""Full name of the site""", json_schema_extra = { "linkml_meta": {'domain_of': ['Site'], 'slot_uri': 'schema:name'} })
    site_description: Optional[str] = Field(default=None, description="""Abbreviated site description""", json_schema_extra = { "linkml_meta": {'domain_of': ['Site'], 'slot_uri': 'schema:description'} })
    site_type: SiteTypeEnum = Field(default=..., description="""Whether site is CORE or GRADIENT""", json_schema_extra = { "linkml_meta": {'domain_of': ['Site']} })
    domain: str = Field(default=..., description="""Domain this site belongs to""", json_schema_extra = { "linkml_meta": {'domain_of': ['Site'], 'slot_uri': 'schema:containedInPlace'} })
    latitude: Optional[Decimal] = Field(default=None, description="""Site latitude in decimal degrees (WGS84)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Site', 'Location', 'GeoCoordinates'], 'slot_uri': 'wgs84:lat'} })
    longitude: Optional[Decimal] = Field(default=None, description="""Site longitude in decimal degrees (WGS84)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Site', 'Location', 'GeoCoordinates'], 'slot_uri': 'wgs84:long'} })
    elevation: Optional[Decimal] = Field(default=None, description="""Site elevation in meters""", json_schema_extra = { "linkml_meta": {'domain_of': ['Site', 'Location', 'GeoCoordinates'],
         'unit': {'ucum_code': 'm'}} })
    state_code: Optional[str] = Field(default=None, description="""Two-letter US state code""", json_schema_extra = { "linkml_meta": {'domain_of': ['Site']} })
    state_name: Optional[str] = Field(default=None, description="""Full state name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Site']} })
    deims_id: Optional[str] = Field(default=None, description="""DEIMS-SDR registry identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Site']} })
    available_data_products: Optional[list[str]] = Field(default=None, description="""Data products available at this site""", json_schema_extra = { "linkml_meta": {'domain_of': ['Site']} })
    locations: Optional[list[str]] = Field(default=None, description="""Named locations within this site""", json_schema_extra = { "linkml_meta": {'domain_of': ['NeonDataset', 'Site']} })


class Location(ConfiguredBaseModel):
    """
    A named location in NEON's hierarchical location system. Locations range from domains to individual sensor positions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Place', 'from_schema': 'https://w3id.org/neon-schema'})

    location_name: str = Field(default=..., description="""Unique location name identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location'], 'slot_uri': 'dcterms:identifier'} })
    location_description: Optional[str] = Field(default=None, description="""Description of the location""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location'], 'slot_uri': 'schema:description'} })
    location_type: Optional[LocationTypeEnum] = Field(default=None, description="""Type of location in hierarchy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location']} })
    site: Optional[str] = Field(default=None, description="""Site this location belongs to""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location',
                       'SiteAvailability',
                       'DataFile',
                       'Sample',
                       'Observation'],
         'slot_uri': 'schema:containedInPlace'} })
    parent_location: Optional[str] = Field(default=None, description="""Parent location in hierarchy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location']} })
    child_locations: Optional[list[str]] = Field(default=None, description="""Child locations in hierarchy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location']} })
    latitude: Optional[Decimal] = Field(default=None, description="""Location latitude in decimal degrees (WGS84)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Site', 'Location', 'GeoCoordinates'], 'slot_uri': 'wgs84:lat'} })
    longitude: Optional[Decimal] = Field(default=None, description="""Location longitude in decimal degrees (WGS84)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Site', 'Location', 'GeoCoordinates'], 'slot_uri': 'wgs84:long'} })
    elevation: Optional[Decimal] = Field(default=None, description="""Location elevation in meters""", json_schema_extra = { "linkml_meta": {'domain_of': ['Site', 'Location', 'GeoCoordinates'],
         'unit': {'ucum_code': 'm'}} })
    utm_easting: Optional[Decimal] = Field(default=None, description="""UTM easting coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location']} })
    utm_northing: Optional[Decimal] = Field(default=None, description="""UTM northing coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location']} })
    utm_zone: Optional[int] = Field(default=None, description="""UTM zone number""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location']} })
    active_periods: Optional[list[TimePeriod]] = Field(default=None, description="""Time periods when location was active""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location']} })


class TimePeriod(ConfiguredBaseModel):
    """
    A time period with start and optional end date
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Schedule', 'from_schema': 'https://w3id.org/neon-schema'})

    start_date: date = Field(default=..., description="""Start date of the period""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimePeriod'], 'slot_uri': 'schema:startDate'} })
    end_date: Optional[date] = Field(default=None, description="""End date of the period (null if ongoing)""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimePeriod'], 'slot_uri': 'schema:endDate'} })


class GeoCoordinates(ConfiguredBaseModel):
    """
    Geographic coordinates
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:GeoCoordinates',
         'from_schema': 'https://w3id.org/neon-schema'})

    latitude: Optional[Decimal] = Field(default=None, description="""Latitude in decimal degrees""", json_schema_extra = { "linkml_meta": {'domain_of': ['Site', 'Location', 'GeoCoordinates'], 'slot_uri': 'wgs84:lat'} })
    longitude: Optional[Decimal] = Field(default=None, description="""Longitude in decimal degrees""", json_schema_extra = { "linkml_meta": {'domain_of': ['Site', 'Location', 'GeoCoordinates'], 'slot_uri': 'wgs84:long'} })
    elevation: Optional[Decimal] = Field(default=None, description="""Elevation in meters""", json_schema_extra = { "linkml_meta": {'domain_of': ['Site', 'Location', 'GeoCoordinates'],
         'unit': {'ucum_code': 'm'}} })


class DataProduct(ConfiguredBaseModel):
    """
    A NEON data product representing a specific type of ecological measurement or observation. Products are identified by codes like DP1.00001.001.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Dataset', 'from_schema': 'https://w3id.org/neon-schema'})

    product_code: str = Field(default=..., description="""Unique product code (e.g., DP1.00001.001)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataProduct'], 'slot_uri': 'dcterms:identifier'} })
    product_name: str = Field(default=..., description="""Human-readable product name""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataProduct'], 'slot_uri': 'schema:name'} })
    product_description: Optional[str] = Field(default=None, description="""Brief description of the product""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataProduct'], 'slot_uri': 'schema:description'} })
    product_abstract: Optional[str] = Field(default=None, description="""Detailed abstract describing the product""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataProduct']} })
    product_status: Optional[ProductStatusEnum] = Field(default=None, description="""Current status of the product""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataProduct']} })
    product_category: Optional[ProductCategoryEnum] = Field(default=None, description="""Processing level category""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataProduct']} })
    product_has_expanded: Optional[bool] = Field(default=None, description="""Whether expanded package is available""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataProduct']} })
    science_team: Optional[str] = Field(default=None, description="""Science team responsible (3-letter abbreviation)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataProduct']} })
    measurement_system: Optional[MeasurementSystemEnum] = Field(default=None, description="""Measurement system that collects this data""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataProduct']} })
    sites: Optional[list[SiteAvailability]] = Field(default=None, description="""Sites where this product is available""", json_schema_extra = { "linkml_meta": {'domain_of': ['NeonDataset', 'Domain', 'DataProduct']} })
    releases: Optional[list[str]] = Field(default=None, description="""Releases containing this product""", json_schema_extra = { "linkml_meta": {'domain_of': ['NeonDataset', 'DataProduct']} })
    specifications: Optional[list[ProductSpecification]] = Field(default=None, description="""Associated protocol and specification documents""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataProduct']} })
    change_logs: Optional[list[ChangeLogEntry]] = Field(default=None, description="""Issues and changes affecting the data""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataProduct']} })
    keywords: Optional[list[str]] = Field(default=None, description="""Keywords describing the product""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataProduct'], 'slot_uri': 'schema:keywords'} })


class SiteAvailability(ConfiguredBaseModel):
    """
    Availability of a data product at a specific site
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/neon-schema'})

    site: str = Field(default=..., description="""Site where data is available""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location',
                       'SiteAvailability',
                       'DataFile',
                       'Sample',
                       'Observation']} })
    available_months: Optional[list[str]] = Field(default=None, description="""Months when data is available (YYYY-MM format)""", json_schema_extra = { "linkml_meta": {'domain_of': ['SiteAvailability']} })
    data_url: Optional[str] = Field(default=None, description="""URL to access the data""", json_schema_extra = { "linkml_meta": {'domain_of': ['SiteAvailability'], 'slot_uri': 'schema:url'} })


class ProductSpecification(ConfiguredBaseModel):
    """
    A specification document associated with a data product
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/neon-schema'})

    spec_id: str = Field(default=..., description="""Unique specification identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProductSpecification']} })
    spec_description: Optional[str] = Field(default=None, description="""Description of the specification""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProductSpecification']} })
    spec_type: Optional[str] = Field(default=None, description="""Type of specification (protocol, user guide, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProductSpecification']} })
    file_name: Optional[str] = Field(default=None, description="""Name of the specification file""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProductSpecification', 'DataFile']} })
    file_size: Optional[int] = Field(default=None, description="""File size in bytes""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProductSpecification', 'ReleaseArtifact', 'DataFile']} })
    mime_type: Optional[str] = Field(default=None, description="""MIME type of the file""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProductSpecification']} })
    url: Optional[str] = Field(default=None, description="""URL to download the specification""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProductSpecification', 'ReleaseArtifact', 'DataFile'],
         'slot_uri': 'schema:url'} })


class ChangeLogEntry(ConfiguredBaseModel):
    """
    A change log entry documenting issues affecting data
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/neon-schema'})

    issue_id: str = Field(default=..., description="""Unique issue identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChangeLogEntry']} })
    parent_issue_id: Optional[str] = Field(default=None, description="""Parent issue ID if this is a sub-issue""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChangeLogEntry']} })
    issue: str = Field(default=..., description="""Description of the issue""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChangeLogEntry']} })
    resolution: Optional[str] = Field(default=None, description="""How the issue was resolved""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChangeLogEntry']} })
    date_range_start: Optional[date] = Field(default=None, description="""Start of affected date range""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChangeLogEntry'], 'slot_uri': 'schema:startDate'} })
    date_range_end: Optional[date] = Field(default=None, description="""End of affected date range""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChangeLogEntry'], 'slot_uri': 'schema:endDate'} })
    locations_affected: Optional[list[str]] = Field(default=None, description="""Locations affected by this issue""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChangeLogEntry']} })
    created_date: Optional[datetime ] = Field(default=None, description="""When the issue was logged""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChangeLogEntry']} })
    resolved_date: Optional[datetime ] = Field(default=None, description="""When the issue was resolved""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChangeLogEntry']} })


class Release(ConfiguredBaseModel):
    """
    A NEON data release - a static, citable collection of data files with a DOI for reproducible research.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:DataCatalog',
         'from_schema': 'https://w3id.org/neon-schema'})

    release_tag: str = Field(default=..., description="""Release identifier (e.g., RELEASE-2025)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Release'], 'slot_uri': 'dcterms:identifier'} })
    uuid: Optional[str] = Field(default=None, description="""Unique UUID for the release""", json_schema_extra = { "linkml_meta": {'domain_of': ['Release']} })
    generation_date: Optional[datetime ] = Field(default=None, description="""Date the release was generated""", json_schema_extra = { "linkml_meta": {'domain_of': ['Release'], 'slot_uri': 'schema:datePublished'} })
    doi: Optional[str] = Field(default=None, description="""Digital Object Identifier for citation""", json_schema_extra = { "linkml_meta": {'domain_of': ['Release'], 'slot_uri': 'dcterms:identifier'} })
    data_products: Optional[list[str]] = Field(default=None, description="""Data products included in this release""", json_schema_extra = { "linkml_meta": {'domain_of': ['NeonDataset', 'Release', 'BiorepositoryCollection']} })
    artifacts: Optional[list[ReleaseArtifact]] = Field(default=None, description="""Downloadable files associated with release""", json_schema_extra = { "linkml_meta": {'domain_of': ['Release']} })
    description: Optional[str] = Field(default=None, description="""Description of the release""", json_schema_extra = { "linkml_meta": {'domain_of': ['Domain', 'Release'], 'slot_uri': 'schema:description'} })


class ReleaseArtifact(ConfiguredBaseModel):
    """
    A downloadable artifact (file) in a release
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/neon-schema'})

    name: str = Field(default=..., description="""File name""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReleaseArtifact'], 'slot_uri': 'schema:name'} })
    artifact_type: Optional[str] = Field(default=None, description="""Type of artifact""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReleaseArtifact']} })
    file_size: Optional[int] = Field(default=None, description="""File size in bytes""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProductSpecification', 'ReleaseArtifact', 'DataFile']} })
    md5_checksum: Optional[str] = Field(default=None, description="""MD5 hash for integrity verification""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReleaseArtifact', 'DataFile']} })
    url: Optional[str] = Field(default=None, description="""Download URL""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProductSpecification', 'ReleaseArtifact', 'DataFile'],
         'slot_uri': 'schema:url'} })


class DataFile(ConfiguredBaseModel):
    """
    An individual data file within a data product
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:DataDownload',
         'from_schema': 'https://w3id.org/neon-schema'})

    file_name: str = Field(default=..., description="""Name of the data file""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProductSpecification', 'DataFile'], 'slot_uri': 'schema:name'} })
    data_product: str = Field(default=..., description="""Data product this file belongs to""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataFile', 'Sample', 'Observation']} })
    site: str = Field(default=..., description="""Site the data was collected at""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location',
                       'SiteAvailability',
                       'DataFile',
                       'Sample',
                       'Observation']} })
    year_month: str = Field(default=..., description="""Month of data collection (YYYY-MM)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataFile']} })
    release: Optional[str] = Field(default=None, description="""Release this file is part of""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataFile', 'Observation']} })
    file_size: Optional[int] = Field(default=None, description="""File size in bytes""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProductSpecification', 'ReleaseArtifact', 'DataFile']} })
    url: Optional[str] = Field(default=None, description="""Download URL (may expire)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProductSpecification', 'ReleaseArtifact', 'DataFile'],
         'slot_uri': 'schema:url'} })
    md5_checksum: Optional[str] = Field(default=None, description="""MD5 hash for integrity verification""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReleaseArtifact', 'DataFile']} })
    crc32_checksum: Optional[str] = Field(default=None, description="""CRC32 checksum""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataFile']} })
    crc32c_checksum: Optional[str] = Field(default=None, description="""CRC32C checksum""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataFile']} })
    package_type: Optional[str] = Field(default=None, description="""Package type (basic or expanded)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataFile']} })


class Sample(ConfiguredBaseModel):
    """
    A physical sample collected by NEON, tracked through the Sample Management System (SMS).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dwc:MaterialSample',
         'from_schema': 'https://w3id.org/neon-schema'})

    sample_uuid: str = Field(default=..., description="""Unique UUID for the sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'], 'slot_uri': 'dwc:materialSampleID'} })
    sample_tag: Optional[str] = Field(default=None, description="""Sample tag identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    sample_class: Optional[str] = Field(default=None, description="""Sample class (ingest table + ID field)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    barcode: Optional[str] = Field(default=None, description="""Sample barcode""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    archive_guid: Optional[str] = Field(default=None, description="""Globally unique archive identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    site: Optional[str] = Field(default=None, description="""Site where sample was collected""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location',
                       'SiteAvailability',
                       'DataFile',
                       'Sample',
                       'Observation'],
         'slot_uri': 'dwc:locationID'} })
    location: Optional[str] = Field(default=None, description="""Specific location where sample was collected""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Observation']} })
    collection_date: Optional[date] = Field(default=None, description="""Date sample was collected""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'], 'slot_uri': 'dwc:eventDate'} })
    taxon: Optional[str] = Field(default=None, description="""Taxonomic identification of sample (if biological)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'BiologicalObservation'], 'slot_uri': 'dwc:taxonID'} })
    parent_samples: Optional[list[str]] = Field(default=None, description="""Parent sample(s) this was derived from""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    child_samples: Optional[list[str]] = Field(default=None, description="""Child samples derived from this sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    data_product: Optional[str] = Field(default=None, description="""Data product this sample is associated with""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataFile', 'Sample', 'Observation']} })
    sample_events: Optional[list[SampleEvent]] = Field(default=None, description="""Custody and processing events""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })


class SampleEvent(ConfiguredBaseModel):
    """
    A custody or processing event for a sample
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/neon-schema'})

    event_id: str = Field(default=..., description="""Unique event identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['SampleEvent']} })
    event_date: Optional[datetime ] = Field(default=None, description="""Date of the event""", json_schema_extra = { "linkml_meta": {'domain_of': ['SampleEvent'], 'slot_uri': 'schema:startDate'} })
    ingest_table_name: Optional[str] = Field(default=None, description="""Name of the data ingest table""", json_schema_extra = { "linkml_meta": {'domain_of': ['SampleEvent']} })
    field_entries: Optional[list[FieldEntry]] = Field(default=None, description="""Field name/value pairs from the event""", json_schema_extra = { "linkml_meta": {'domain_of': ['SampleEvent']} })


class FieldEntry(ConfiguredBaseModel):
    """
    A field name/value pair from a sample event
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/neon-schema'})

    field_name: str = Field(default=..., description="""Name of the field""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldEntry']} })
    field_value: Optional[str] = Field(default=None, description="""Value of the field""", json_schema_extra = { "linkml_meta": {'domain_of': ['FieldEntry']} })


class Taxon(ConfiguredBaseModel):
    """
    A taxonomic record from NEON's taxon lists, following Darwin Core standards. Taxa are compiled from published sources for field staff verification.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dwc:Taxon', 'from_schema': 'https://w3id.org/neon-schema'})

    taxon_id: str = Field(default=..., description="""Unique taxon identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Taxon'], 'slot_uri': 'dwc:taxonID'} })
    accepted_taxon_id: Optional[str] = Field(default=None, description="""ID of accepted taxon if this is a synonym""", json_schema_extra = { "linkml_meta": {'domain_of': ['Taxon'], 'slot_uri': 'dwc:acceptedNameUsageID'} })
    taxon_type: TaxonTypeEnum = Field(default=..., description="""Major taxonomic grouping (BIRD, PLANT, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Taxon']} })
    scientific_name: str = Field(default=..., description="""Full scientific name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Taxon'], 'slot_uri': 'dwc:scientificName'} })
    scientific_name_authorship: Optional[str] = Field(default=None, description="""Authorship of the scientific name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Taxon'], 'slot_uri': 'dwc:scientificNameAuthorship'} })
    vernacular_name: Optional[str] = Field(default=None, description="""Common name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Taxon'], 'slot_uri': 'dwc:vernacularName'} })
    taxon_rank: Optional[str] = Field(default=None, description="""Taxonomic rank (species, genus, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Taxon'], 'slot_uri': 'dwc:taxonRank'} })
    kingdom: Optional[str] = Field(default=None, description="""Kingdom classification""", json_schema_extra = { "linkml_meta": {'domain_of': ['Taxon'], 'slot_uri': 'dwc:kingdom'} })
    phylum: Optional[str] = Field(default=None, description="""Phylum classification""", json_schema_extra = { "linkml_meta": {'domain_of': ['Taxon'], 'slot_uri': 'dwc:phylum'} })
    class_name: Optional[str] = Field(default=None, description="""Class classification""", json_schema_extra = { "linkml_meta": {'domain_of': ['Taxon'], 'slot_uri': 'dwc:class'} })
    order: Optional[str] = Field(default=None, description="""Order classification""", json_schema_extra = { "linkml_meta": {'domain_of': ['Taxon'], 'slot_uri': 'dwc:order'} })
    family: Optional[str] = Field(default=None, description="""Family classification""", json_schema_extra = { "linkml_meta": {'domain_of': ['Taxon'], 'slot_uri': 'dwc:family'} })
    genus: Optional[str] = Field(default=None, description="""Genus classification""", json_schema_extra = { "linkml_meta": {'domain_of': ['Taxon'], 'slot_uri': 'dwc:genus'} })
    species: Optional[str] = Field(default=None, description="""Species epithet""", json_schema_extra = { "linkml_meta": {'domain_of': ['Taxon'], 'slot_uri': 'dwc:specificEpithet'} })
    subspecies: Optional[str] = Field(default=None, description="""Subspecies epithet""", json_schema_extra = { "linkml_meta": {'domain_of': ['Taxon'], 'slot_uri': 'dwc:infraspecificEpithet'} })
    gbif_rank: Optional[str] = Field(default=None, description="""GBIF vocabulary rank for subspecific taxa""", json_schema_extra = { "linkml_meta": {'domain_of': ['Taxon']} })
    native_status_code: Optional[str] = Field(default=None, description="""Native/introduced status codes by region""", json_schema_extra = { "linkml_meta": {'domain_of': ['Taxon']} })
    update_date: Optional[date] = Field(default=None, description="""Date of last taxonomic update""", json_schema_extra = { "linkml_meta": {'domain_of': ['Taxon'], 'slot_uri': 'dcterms:modified'} })


class Observation(ConfiguredBaseModel):
    """
    A generic observation or measurement record from NEON. This is a base class for specific observation types.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Observation',
         'from_schema': 'https://w3id.org/neon-schema'})

    observation_id: str = Field(default=..., description="""Unique observation identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Observation'], 'slot_uri': 'dcterms:identifier'} })
    site: str = Field(default=..., description="""Site where observation was made""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location',
                       'SiteAvailability',
                       'DataFile',
                       'Sample',
                       'Observation'],
         'slot_uri': 'dwc:locationID'} })
    location: Optional[str] = Field(default=None, description="""Specific location of observation""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Observation']} })
    data_product: str = Field(default=..., description="""Data product this observation belongs to""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataFile', 'Sample', 'Observation']} })
    observation_datetime: datetime  = Field(default=..., description="""Date and time of observation""", json_schema_extra = { "linkml_meta": {'domain_of': ['Observation'], 'slot_uri': 'dwc:eventDate'} })
    release: Optional[str] = Field(default=None, description="""Release this observation is from""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataFile', 'Observation']} })


class BiologicalObservation(Observation):
    """
    An observation of a biological organism
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/neon-schema'})

    taxon: Optional[str] = Field(default=None, description="""Taxonomic identification""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'BiologicalObservation'], 'slot_uri': 'dwc:taxonID'} })
    individual_count: Optional[int] = Field(default=None, description="""Number of individuals observed""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiologicalObservation'], 'slot_uri': 'dwc:individualCount'} })
    occurrence_status: Optional[str] = Field(default=None, description="""Presence/absence status""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiologicalObservation'], 'slot_uri': 'dwc:occurrenceStatus'} })
    sample: Optional[str] = Field(default=None, description="""Associated sample if collected""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiologicalObservation']} })
    observation_id: str = Field(default=..., description="""Unique observation identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Observation'], 'slot_uri': 'dcterms:identifier'} })
    site: str = Field(default=..., description="""Site where observation was made""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location',
                       'SiteAvailability',
                       'DataFile',
                       'Sample',
                       'Observation'],
         'slot_uri': 'dwc:locationID'} })
    location: Optional[str] = Field(default=None, description="""Specific location of observation""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Observation']} })
    data_product: str = Field(default=..., description="""Data product this observation belongs to""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataFile', 'Sample', 'Observation']} })
    observation_datetime: datetime  = Field(default=..., description="""Date and time of observation""", json_schema_extra = { "linkml_meta": {'domain_of': ['Observation'], 'slot_uri': 'dwc:eventDate'} })
    release: Optional[str] = Field(default=None, description="""Release this observation is from""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataFile', 'Observation']} })


class EnvironmentalObservation(Observation):
    """
    An environmental or instrumental measurement
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/neon-schema'})

    measured_property: str = Field(default=..., description="""Property being measured""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnvironmentalObservation']} })
    measurement_value: Optional[Decimal] = Field(default=None, description="""Numeric value of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnvironmentalObservation']} })
    measurement_unit: Optional[str] = Field(default=None, description="""Unit of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnvironmentalObservation']} })
    quality_flag: Optional[str] = Field(default=None, description="""Data quality flag""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnvironmentalObservation']} })
    sensor_location: Optional[str] = Field(default=None, description="""Location of the sensor""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnvironmentalObservation']} })
    observation_id: str = Field(default=..., description="""Unique observation identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Observation'], 'slot_uri': 'dcterms:identifier'} })
    site: str = Field(default=..., description="""Site where observation was made""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location',
                       'SiteAvailability',
                       'DataFile',
                       'Sample',
                       'Observation'],
         'slot_uri': 'dwc:locationID'} })
    location: Optional[str] = Field(default=None, description="""Specific location of observation""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Observation']} })
    data_product: str = Field(default=..., description="""Data product this observation belongs to""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataFile', 'Sample', 'Observation']} })
    observation_datetime: datetime  = Field(default=..., description="""Date and time of observation""", json_schema_extra = { "linkml_meta": {'domain_of': ['Observation'], 'slot_uri': 'dwc:eventDate'} })
    release: Optional[str] = Field(default=None, description="""Release this observation is from""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataFile', 'Observation']} })


class BiorepositoryCollection(ConfiguredBaseModel):
    """
    A collection of samples held in a biorepository
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/neon-schema'})

    collection_code: str = Field(default=..., description="""Unique collection code""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiorepositoryCollection'], 'slot_uri': 'dcterms:identifier'} })
    collection_name: str = Field(default=..., description="""Name of the collection""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiorepositoryCollection'], 'slot_uri': 'schema:name'} })
    collection_url: Optional[str] = Field(default=None, description="""URL for the collection""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiorepositoryCollection'], 'slot_uri': 'schema:url'} })
    data_products: Optional[list[str]] = Field(default=None, description="""Data products associated with this collection""", json_schema_extra = { "linkml_meta": {'domain_of': ['NeonDataset', 'Release', 'BiorepositoryCollection']} })
    samples: Optional[list[str]] = Field(default=None, description="""Samples in this collection""", json_schema_extra = { "linkml_meta": {'domain_of': ['NeonDataset', 'BiorepositoryCollection']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NeonDataset.model_rebuild()
Domain.model_rebuild()
Site.model_rebuild()
Location.model_rebuild()
TimePeriod.model_rebuild()
GeoCoordinates.model_rebuild()
DataProduct.model_rebuild()
SiteAvailability.model_rebuild()
ProductSpecification.model_rebuild()
ChangeLogEntry.model_rebuild()
Release.model_rebuild()
ReleaseArtifact.model_rebuild()
DataFile.model_rebuild()
Sample.model_rebuild()
SampleEvent.model_rebuild()
FieldEntry.model_rebuild()
Taxon.model_rebuild()
Observation.model_rebuild()
BiologicalObservation.model_rebuild()
EnvironmentalObservation.model_rebuild()
BiorepositoryCollection.model_rebuild()
