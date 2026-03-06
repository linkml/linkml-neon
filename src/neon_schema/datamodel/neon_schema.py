/Users/athessen/linkml-neon/.venv/lib/python3.12/site-packages/requests/__init__.py:113: RequestsDependencyWarning: urllib3 (2.6.3) or chardet (7.0.1)/charset_normalizer (3.4.5) doesn't match a supported version!
  warnings.warn(
# Auto generated from neon_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-03-06T11:02:45
# Schema: neon_schema
#
# id: https://w3id.org/neon-schema
# description: LinkML schema for National Ecological Observatory Network (NEON) data. This schema models NEON's hierarchical data structure including domains, sites, locations, data products, samples, and taxonomic information with cross-links between entities.
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Date, Datetime, Decimal, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, Decimal, URI, XSDDate, XSDDateTime

metamodel_version = "1.7.0"
version = "0.1.0"

# Namespaces
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DWC = CurieNamespace('dwc', 'http://rs.tdwg.org/dwc/terms/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NEON = CurieNamespace('neon', 'https://w3id.org/neon-schema/')
ORCID = CurieNamespace('orcid', 'https://orcid.org/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
WGS84 = CurieNamespace('wgs84', 'http://www.w3.org/2003/01/geo/wgs84_pos#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = NEON


# Types
class DomainCode(String):
    """ Domain code in format D01-D20 """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "DomainCode"
    type_model_uri = NEON.DomainCode


class SiteCode(String):
    """ Four-character site code """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "SiteCode"
    type_model_uri = NEON.SiteCode


class ProductCode(String):
    """ Data product code in format DPX.XXXXX.XXX """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ProductCode"
    type_model_uri = NEON.ProductCode


class YearMonth(String):
    """ Year-month in YYYY-MM format """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "YearMonth"
    type_model_uri = NEON.YearMonth


# Class references
class DomainDomainCode(DomainCode):
    pass


class SiteSiteCode(SiteCode):
    pass


class LocationLocationName(extended_str):
    pass


class DataProductProductCode(ProductCode):
    pass


class ProductSpecificationSpecId(extended_str):
    pass


class ChangeLogEntryIssueId(extended_str):
    pass


class ReleaseReleaseTag(extended_str):
    pass


class DataFileFileName(extended_str):
    pass


class SampleSampleUuid(extended_str):
    pass


class SampleEventEventId(extended_str):
    pass


class TaxonTaxonId(extended_str):
    pass


class ObservationObservationId(extended_str):
    pass


class BiologicalObservationObservationId(ObservationObservationId):
    pass


class EnvironmentalObservationObservationId(ObservationObservationId):
    pass


class BiorepositoryCollectionCollectionCode(extended_str):
    pass


@dataclass(repr=False)
class NeonDataset(YAMLRoot):
    """
    Container for a collection of NEON data entities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NEON["NeonDataset"]
    class_class_curie: ClassVar[str] = "neon:NeonDataset"
    class_name: ClassVar[str] = "NeonDataset"
    class_model_uri: ClassVar[URIRef] = NEON.NeonDataset

    domains: Optional[Union[dict[Union[str, DomainDomainCode], Union[dict, "Domain"]], list[Union[dict, "Domain"]]]] = empty_dict()
    sites: Optional[Union[dict[Union[str, SiteSiteCode], Union[dict, "Site"]], list[Union[dict, "Site"]]]] = empty_dict()
    locations: Optional[Union[dict[Union[str, LocationLocationName], Union[dict, "Location"]], list[Union[dict, "Location"]]]] = empty_dict()
    data_products: Optional[Union[dict[Union[str, DataProductProductCode], Union[dict, "DataProduct"]], list[Union[dict, "DataProduct"]]]] = empty_dict()
    releases: Optional[Union[dict[Union[str, ReleaseReleaseTag], Union[dict, "Release"]], list[Union[dict, "Release"]]]] = empty_dict()
    taxa: Optional[Union[dict[Union[str, TaxonTaxonId], Union[dict, "Taxon"]], list[Union[dict, "Taxon"]]]] = empty_dict()
    samples: Optional[Union[dict[Union[str, SampleSampleUuid], Union[dict, "Sample"]], list[Union[dict, "Sample"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="domains", slot_type=Domain, key_name="domain_code", keyed=True)

        self._normalize_inlined_as_list(slot_name="sites", slot_type=Site, key_name="site_code", keyed=True)

        self._normalize_inlined_as_list(slot_name="locations", slot_type=Location, key_name="location_name", keyed=True)

        self._normalize_inlined_as_list(slot_name="data_products", slot_type=DataProduct, key_name="product_code", keyed=True)

        self._normalize_inlined_as_list(slot_name="releases", slot_type=Release, key_name="release_tag", keyed=True)

        self._normalize_inlined_as_list(slot_name="taxa", slot_type=Taxon, key_name="taxon_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="samples", slot_type=Sample, key_name="sample_uuid", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Domain(YAMLRoot):
    """
    A NEON domain representing a distinct eco-climatic region. NEON divides the US into 20 eco-climatic domains.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Place"]
    class_class_curie: ClassVar[str] = "schema:Place"
    class_name: ClassVar[str] = "Domain"
    class_model_uri: ClassVar[URIRef] = NEON.Domain

    domain_code: Union[str, DomainDomainCode] = None
    domain_name: str = None
    description: Optional[str] = None
    sites: Optional[Union[Union[str, SiteSiteCode], list[Union[str, SiteSiteCode]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.domain_code):
            self.MissingRequiredField("domain_code")
        if not isinstance(self.domain_code, DomainDomainCode):
            self.domain_code = DomainDomainCode(self.domain_code)

        if self._is_empty(self.domain_name):
            self.MissingRequiredField("domain_name")
        if not isinstance(self.domain_name, str):
            self.domain_name = str(self.domain_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.sites, list):
            self.sites = [self.sites] if self.sites is not None else []
        self.sites = [v if isinstance(v, SiteSiteCode) else SiteSiteCode(v) for v in self.sites]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Site(YAMLRoot):
    """
    A NEON field site where data collection occurs. Sites are either CORE (representing key ecosystems) or GRADIENT
    (capturing environmental gradients).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Place"]
    class_class_curie: ClassVar[str] = "schema:Place"
    class_name: ClassVar[str] = "Site"
    class_model_uri: ClassVar[URIRef] = NEON.Site

    site_code: Union[str, SiteSiteCode] = None
    site_name: str = None
    site_type: Union[str, "SiteTypeEnum"] = None
    domain: Union[str, DomainDomainCode] = None
    site_description: Optional[str] = None
    latitude: Optional[Decimal] = None
    longitude: Optional[Decimal] = None
    elevation: Optional[Decimal] = None
    state_code: Optional[str] = None
    state_name: Optional[str] = None
    deims_id: Optional[str] = None
    available_data_products: Optional[Union[Union[str, DataProductProductCode], list[Union[str, DataProductProductCode]]]] = empty_list()
    locations: Optional[Union[Union[str, LocationLocationName], list[Union[str, LocationLocationName]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.site_code):
            self.MissingRequiredField("site_code")
        if not isinstance(self.site_code, SiteSiteCode):
            self.site_code = SiteSiteCode(self.site_code)

        if self._is_empty(self.site_name):
            self.MissingRequiredField("site_name")
        if not isinstance(self.site_name, str):
            self.site_name = str(self.site_name)

        if self._is_empty(self.site_type):
            self.MissingRequiredField("site_type")
        if not isinstance(self.site_type, SiteTypeEnum):
            self.site_type = SiteTypeEnum(self.site_type)

        if self._is_empty(self.domain):
            self.MissingRequiredField("domain")
        if not isinstance(self.domain, DomainDomainCode):
            self.domain = DomainDomainCode(self.domain)

        if self.site_description is not None and not isinstance(self.site_description, str):
            self.site_description = str(self.site_description)

        if self.latitude is not None and not isinstance(self.latitude, Decimal):
            self.latitude = Decimal(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, Decimal):
            self.longitude = Decimal(self.longitude)

        if self.elevation is not None and not isinstance(self.elevation, Decimal):
            self.elevation = Decimal(self.elevation)

        if self.state_code is not None and not isinstance(self.state_code, str):
            self.state_code = str(self.state_code)

        if self.state_name is not None and not isinstance(self.state_name, str):
            self.state_name = str(self.state_name)

        if self.deims_id is not None and not isinstance(self.deims_id, str):
            self.deims_id = str(self.deims_id)

        if not isinstance(self.available_data_products, list):
            self.available_data_products = [self.available_data_products] if self.available_data_products is not None else []
        self.available_data_products = [v if isinstance(v, DataProductProductCode) else DataProductProductCode(v) for v in self.available_data_products]

        if not isinstance(self.locations, list):
            self.locations = [self.locations] if self.locations is not None else []
        self.locations = [v if isinstance(v, LocationLocationName) else LocationLocationName(v) for v in self.locations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Location(YAMLRoot):
    """
    A named location in NEON's hierarchical location system. Locations range from domains to individual sensor
    positions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Place"]
    class_class_curie: ClassVar[str] = "schema:Place"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = NEON.Location

    location_name: Union[str, LocationLocationName] = None
    location_description: Optional[str] = None
    location_type: Optional[Union[str, "LocationTypeEnum"]] = None
    site: Optional[Union[str, SiteSiteCode]] = None
    parent_location: Optional[Union[str, LocationLocationName]] = None
    child_locations: Optional[Union[Union[str, LocationLocationName], list[Union[str, LocationLocationName]]]] = empty_list()
    latitude: Optional[Decimal] = None
    longitude: Optional[Decimal] = None
    elevation: Optional[Decimal] = None
    utm_easting: Optional[Decimal] = None
    utm_northing: Optional[Decimal] = None
    utm_zone: Optional[int] = None
    active_periods: Optional[Union[Union[dict, "TimePeriod"], list[Union[dict, "TimePeriod"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.location_name):
            self.MissingRequiredField("location_name")
        if not isinstance(self.location_name, LocationLocationName):
            self.location_name = LocationLocationName(self.location_name)

        if self.location_description is not None and not isinstance(self.location_description, str):
            self.location_description = str(self.location_description)

        if self.location_type is not None and not isinstance(self.location_type, LocationTypeEnum):
            self.location_type = LocationTypeEnum(self.location_type)

        if self.site is not None and not isinstance(self.site, SiteSiteCode):
            self.site = SiteSiteCode(self.site)

        if self.parent_location is not None and not isinstance(self.parent_location, LocationLocationName):
            self.parent_location = LocationLocationName(self.parent_location)

        if not isinstance(self.child_locations, list):
            self.child_locations = [self.child_locations] if self.child_locations is not None else []
        self.child_locations = [v if isinstance(v, LocationLocationName) else LocationLocationName(v) for v in self.child_locations]

        if self.latitude is not None and not isinstance(self.latitude, Decimal):
            self.latitude = Decimal(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, Decimal):
            self.longitude = Decimal(self.longitude)

        if self.elevation is not None and not isinstance(self.elevation, Decimal):
            self.elevation = Decimal(self.elevation)

        if self.utm_easting is not None and not isinstance(self.utm_easting, Decimal):
            self.utm_easting = Decimal(self.utm_easting)

        if self.utm_northing is not None and not isinstance(self.utm_northing, Decimal):
            self.utm_northing = Decimal(self.utm_northing)

        if self.utm_zone is not None and not isinstance(self.utm_zone, int):
            self.utm_zone = int(self.utm_zone)

        self._normalize_inlined_as_list(slot_name="active_periods", slot_type=TimePeriod, key_name="start_date", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TimePeriod(YAMLRoot):
    """
    A time period with start and optional end date
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Schedule"]
    class_class_curie: ClassVar[str] = "schema:Schedule"
    class_name: ClassVar[str] = "TimePeriod"
    class_model_uri: ClassVar[URIRef] = NEON.TimePeriod

    start_date: Union[str, XSDDate] = None
    end_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.start_date):
            self.MissingRequiredField("start_date")
        if not isinstance(self.start_date, XSDDate):
            self.start_date = XSDDate(self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, XSDDate):
            self.end_date = XSDDate(self.end_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeoCoordinates(YAMLRoot):
    """
    Geographic coordinates
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["GeoCoordinates"]
    class_class_curie: ClassVar[str] = "schema:GeoCoordinates"
    class_name: ClassVar[str] = "GeoCoordinates"
    class_model_uri: ClassVar[URIRef] = NEON.GeoCoordinates

    latitude: Optional[Decimal] = None
    longitude: Optional[Decimal] = None
    elevation: Optional[Decimal] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.latitude is not None and not isinstance(self.latitude, Decimal):
            self.latitude = Decimal(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, Decimal):
            self.longitude = Decimal(self.longitude)

        if self.elevation is not None and not isinstance(self.elevation, Decimal):
            self.elevation = Decimal(self.elevation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataProduct(YAMLRoot):
    """
    A NEON data product representing a specific type of ecological measurement or observation. Products are identified
    by codes like DP1.00001.001.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Dataset"]
    class_class_curie: ClassVar[str] = "schema:Dataset"
    class_name: ClassVar[str] = "DataProduct"
    class_model_uri: ClassVar[URIRef] = NEON.DataProduct

    product_code: Union[str, DataProductProductCode] = None
    product_name: str = None
    product_description: Optional[str] = None
    product_abstract: Optional[str] = None
    product_status: Optional[Union[str, "ProductStatusEnum"]] = None
    product_category: Optional[Union[str, "ProductCategoryEnum"]] = None
    product_has_expanded: Optional[Union[bool, Bool]] = None
    science_team: Optional[str] = None
    measurement_system: Optional[Union[str, "MeasurementSystemEnum"]] = None
    sites: Optional[Union[Union[dict, "SiteAvailability"], list[Union[dict, "SiteAvailability"]]]] = empty_list()
    releases: Optional[Union[Union[str, ReleaseReleaseTag], list[Union[str, ReleaseReleaseTag]]]] = empty_list()
    specifications: Optional[Union[dict[Union[str, ProductSpecificationSpecId], Union[dict, "ProductSpecification"]], list[Union[dict, "ProductSpecification"]]]] = empty_dict()
    change_logs: Optional[Union[dict[Union[str, ChangeLogEntryIssueId], Union[dict, "ChangeLogEntry"]], list[Union[dict, "ChangeLogEntry"]]]] = empty_dict()
    keywords: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.product_code):
            self.MissingRequiredField("product_code")
        if not isinstance(self.product_code, DataProductProductCode):
            self.product_code = DataProductProductCode(self.product_code)

        if self._is_empty(self.product_name):
            self.MissingRequiredField("product_name")
        if not isinstance(self.product_name, str):
            self.product_name = str(self.product_name)

        if self.product_description is not None and not isinstance(self.product_description, str):
            self.product_description = str(self.product_description)

        if self.product_abstract is not None and not isinstance(self.product_abstract, str):
            self.product_abstract = str(self.product_abstract)

        if self.product_status is not None and not isinstance(self.product_status, ProductStatusEnum):
            self.product_status = ProductStatusEnum(self.product_status)

        if self.product_category is not None and not isinstance(self.product_category, ProductCategoryEnum):
            self.product_category = ProductCategoryEnum(self.product_category)

        if self.product_has_expanded is not None and not isinstance(self.product_has_expanded, Bool):
            self.product_has_expanded = Bool(self.product_has_expanded)

        if self.science_team is not None and not isinstance(self.science_team, str):
            self.science_team = str(self.science_team)

        if self.measurement_system is not None and not isinstance(self.measurement_system, MeasurementSystemEnum):
            self.measurement_system = MeasurementSystemEnum(self.measurement_system)

        if not isinstance(self.sites, list):
            self.sites = [self.sites] if self.sites is not None else []
        self.sites = [v if isinstance(v, SiteAvailability) else SiteAvailability(**as_dict(v)) for v in self.sites]

        if not isinstance(self.releases, list):
            self.releases = [self.releases] if self.releases is not None else []
        self.releases = [v if isinstance(v, ReleaseReleaseTag) else ReleaseReleaseTag(v) for v in self.releases]

        self._normalize_inlined_as_list(slot_name="specifications", slot_type=ProductSpecification, key_name="spec_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="change_logs", slot_type=ChangeLogEntry, key_name="issue_id", keyed=True)

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SiteAvailability(YAMLRoot):
    """
    Availability of a data product at a specific site
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NEON["SiteAvailability"]
    class_class_curie: ClassVar[str] = "neon:SiteAvailability"
    class_name: ClassVar[str] = "SiteAvailability"
    class_model_uri: ClassVar[URIRef] = NEON.SiteAvailability

    site: Union[str, SiteSiteCode] = None
    available_months: Optional[Union[Union[str, YearMonth], list[Union[str, YearMonth]]]] = empty_list()
    data_url: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.site):
            self.MissingRequiredField("site")
        if not isinstance(self.site, SiteSiteCode):
            self.site = SiteSiteCode(self.site)

        if not isinstance(self.available_months, list):
            self.available_months = [self.available_months] if self.available_months is not None else []
        self.available_months = [v if isinstance(v, YearMonth) else YearMonth(v) for v in self.available_months]

        if self.data_url is not None and not isinstance(self.data_url, URI):
            self.data_url = URI(self.data_url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProductSpecification(YAMLRoot):
    """
    A specification document associated with a data product
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NEON["ProductSpecification"]
    class_class_curie: ClassVar[str] = "neon:ProductSpecification"
    class_name: ClassVar[str] = "ProductSpecification"
    class_model_uri: ClassVar[URIRef] = NEON.ProductSpecification

    spec_id: Union[str, ProductSpecificationSpecId] = None
    spec_description: Optional[str] = None
    spec_type: Optional[str] = None
    file_name: Optional[str] = None
    file_size: Optional[int] = None
    mime_type: Optional[str] = None
    url: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spec_id):
            self.MissingRequiredField("spec_id")
        if not isinstance(self.spec_id, ProductSpecificationSpecId):
            self.spec_id = ProductSpecificationSpecId(self.spec_id)

        if self.spec_description is not None and not isinstance(self.spec_description, str):
            self.spec_description = str(self.spec_description)

        if self.spec_type is not None and not isinstance(self.spec_type, str):
            self.spec_type = str(self.spec_type)

        if self.file_name is not None and not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self.file_size is not None and not isinstance(self.file_size, int):
            self.file_size = int(self.file_size)

        if self.mime_type is not None and not isinstance(self.mime_type, str):
            self.mime_type = str(self.mime_type)

        if self.url is not None and not isinstance(self.url, URI):
            self.url = URI(self.url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChangeLogEntry(YAMLRoot):
    """
    A change log entry documenting issues affecting data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NEON["ChangeLogEntry"]
    class_class_curie: ClassVar[str] = "neon:ChangeLogEntry"
    class_name: ClassVar[str] = "ChangeLogEntry"
    class_model_uri: ClassVar[URIRef] = NEON.ChangeLogEntry

    issue_id: Union[str, ChangeLogEntryIssueId] = None
    issue: str = None
    parent_issue_id: Optional[str] = None
    resolution: Optional[str] = None
    date_range_start: Optional[Union[str, XSDDate]] = None
    date_range_end: Optional[Union[str, XSDDate]] = None
    locations_affected: Optional[Union[Union[str, LocationLocationName], list[Union[str, LocationLocationName]]]] = empty_list()
    created_date: Optional[Union[str, XSDDateTime]] = None
    resolved_date: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.issue_id):
            self.MissingRequiredField("issue_id")
        if not isinstance(self.issue_id, ChangeLogEntryIssueId):
            self.issue_id = ChangeLogEntryIssueId(self.issue_id)

        if self._is_empty(self.issue):
            self.MissingRequiredField("issue")
        if not isinstance(self.issue, str):
            self.issue = str(self.issue)

        if self.parent_issue_id is not None and not isinstance(self.parent_issue_id, str):
            self.parent_issue_id = str(self.parent_issue_id)

        if self.resolution is not None and not isinstance(self.resolution, str):
            self.resolution = str(self.resolution)

        if self.date_range_start is not None and not isinstance(self.date_range_start, XSDDate):
            self.date_range_start = XSDDate(self.date_range_start)

        if self.date_range_end is not None and not isinstance(self.date_range_end, XSDDate):
            self.date_range_end = XSDDate(self.date_range_end)

        if not isinstance(self.locations_affected, list):
            self.locations_affected = [self.locations_affected] if self.locations_affected is not None else []
        self.locations_affected = [v if isinstance(v, LocationLocationName) else LocationLocationName(v) for v in self.locations_affected]

        if self.created_date is not None and not isinstance(self.created_date, XSDDateTime):
            self.created_date = XSDDateTime(self.created_date)

        if self.resolved_date is not None and not isinstance(self.resolved_date, XSDDateTime):
            self.resolved_date = XSDDateTime(self.resolved_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Release(YAMLRoot):
    """
    A NEON data release - a static, citable collection of data files with a DOI for reproducible research.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["DataCatalog"]
    class_class_curie: ClassVar[str] = "schema:DataCatalog"
    class_name: ClassVar[str] = "Release"
    class_model_uri: ClassVar[URIRef] = NEON.Release

    release_tag: Union[str, ReleaseReleaseTag] = None
    uuid: Optional[str] = None
    generation_date: Optional[Union[str, XSDDateTime]] = None
    doi: Optional[str] = None
    data_products: Optional[Union[Union[str, DataProductProductCode], list[Union[str, DataProductProductCode]]]] = empty_list()
    artifacts: Optional[Union[Union[dict, "ReleaseArtifact"], list[Union[dict, "ReleaseArtifact"]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.release_tag):
            self.MissingRequiredField("release_tag")
        if not isinstance(self.release_tag, ReleaseReleaseTag):
            self.release_tag = ReleaseReleaseTag(self.release_tag)

        if self.uuid is not None and not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self.generation_date is not None and not isinstance(self.generation_date, XSDDateTime):
            self.generation_date = XSDDateTime(self.generation_date)

        if self.doi is not None and not isinstance(self.doi, str):
            self.doi = str(self.doi)

        if not isinstance(self.data_products, list):
            self.data_products = [self.data_products] if self.data_products is not None else []
        self.data_products = [v if isinstance(v, DataProductProductCode) else DataProductProductCode(v) for v in self.data_products]

        self._normalize_inlined_as_list(slot_name="artifacts", slot_type=ReleaseArtifact, key_name="name", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReleaseArtifact(YAMLRoot):
    """
    A downloadable artifact (file) in a release
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NEON["ReleaseArtifact"]
    class_class_curie: ClassVar[str] = "neon:ReleaseArtifact"
    class_name: ClassVar[str] = "ReleaseArtifact"
    class_model_uri: ClassVar[URIRef] = NEON.ReleaseArtifact

    name: str = None
    artifact_type: Optional[str] = None
    file_size: Optional[int] = None
    md5_checksum: Optional[str] = None
    url: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.artifact_type is not None and not isinstance(self.artifact_type, str):
            self.artifact_type = str(self.artifact_type)

        if self.file_size is not None and not isinstance(self.file_size, int):
            self.file_size = int(self.file_size)

        if self.md5_checksum is not None and not isinstance(self.md5_checksum, str):
            self.md5_checksum = str(self.md5_checksum)

        if self.url is not None and not isinstance(self.url, URI):
            self.url = URI(self.url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataFile(YAMLRoot):
    """
    An individual data file within a data product
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["DataDownload"]
    class_class_curie: ClassVar[str] = "schema:DataDownload"
    class_name: ClassVar[str] = "DataFile"
    class_model_uri: ClassVar[URIRef] = NEON.DataFile

    file_name: Union[str, DataFileFileName] = None
    data_product: Union[str, DataProductProductCode] = None
    site: Union[str, SiteSiteCode] = None
    year_month: Union[str, YearMonth] = None
    release: Optional[Union[str, ReleaseReleaseTag]] = None
    file_size: Optional[int] = None
    url: Optional[Union[str, URI]] = None
    md5_checksum: Optional[str] = None
    crc32_checksum: Optional[str] = None
    crc32c_checksum: Optional[str] = None
    package_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.file_name):
            self.MissingRequiredField("file_name")
        if not isinstance(self.file_name, DataFileFileName):
            self.file_name = DataFileFileName(self.file_name)

        if self._is_empty(self.data_product):
            self.MissingRequiredField("data_product")
        if not isinstance(self.data_product, DataProductProductCode):
            self.data_product = DataProductProductCode(self.data_product)

        if self._is_empty(self.site):
            self.MissingRequiredField("site")
        if not isinstance(self.site, SiteSiteCode):
            self.site = SiteSiteCode(self.site)

        if self._is_empty(self.year_month):
            self.MissingRequiredField("year_month")
        if not isinstance(self.year_month, YearMonth):
            self.year_month = YearMonth(self.year_month)

        if self.release is not None and not isinstance(self.release, ReleaseReleaseTag):
            self.release = ReleaseReleaseTag(self.release)

        if self.file_size is not None and not isinstance(self.file_size, int):
            self.file_size = int(self.file_size)

        if self.url is not None and not isinstance(self.url, URI):
            self.url = URI(self.url)

        if self.md5_checksum is not None and not isinstance(self.md5_checksum, str):
            self.md5_checksum = str(self.md5_checksum)

        if self.crc32_checksum is not None and not isinstance(self.crc32_checksum, str):
            self.crc32_checksum = str(self.crc32_checksum)

        if self.crc32c_checksum is not None and not isinstance(self.crc32c_checksum, str):
            self.crc32c_checksum = str(self.crc32c_checksum)

        if self.package_type is not None and not isinstance(self.package_type, str):
            self.package_type = str(self.package_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sample(YAMLRoot):
    """
    A physical sample collected by NEON, tracked through the Sample Management System (SMS).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC["MaterialSample"]
    class_class_curie: ClassVar[str] = "dwc:MaterialSample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = NEON.Sample

    sample_uuid: Union[str, SampleSampleUuid] = None
    sample_tag: Optional[str] = None
    sample_class: Optional[str] = None
    barcode: Optional[str] = None
    archive_guid: Optional[str] = None
    site: Optional[Union[str, SiteSiteCode]] = None
    location: Optional[Union[str, LocationLocationName]] = None
    collection_date: Optional[Union[str, XSDDate]] = None
    taxon: Optional[Union[str, TaxonTaxonId]] = None
    parent_samples: Optional[Union[Union[str, SampleSampleUuid], list[Union[str, SampleSampleUuid]]]] = empty_list()
    child_samples: Optional[Union[Union[str, SampleSampleUuid], list[Union[str, SampleSampleUuid]]]] = empty_list()
    data_product: Optional[Union[str, DataProductProductCode]] = None
    sample_events: Optional[Union[dict[Union[str, SampleEventEventId], Union[dict, "SampleEvent"]], list[Union[dict, "SampleEvent"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.sample_uuid):
            self.MissingRequiredField("sample_uuid")
        if not isinstance(self.sample_uuid, SampleSampleUuid):
            self.sample_uuid = SampleSampleUuid(self.sample_uuid)

        if self.sample_tag is not None and not isinstance(self.sample_tag, str):
            self.sample_tag = str(self.sample_tag)

        if self.sample_class is not None and not isinstance(self.sample_class, str):
            self.sample_class = str(self.sample_class)

        if self.barcode is not None and not isinstance(self.barcode, str):
            self.barcode = str(self.barcode)

        if self.archive_guid is not None and not isinstance(self.archive_guid, str):
            self.archive_guid = str(self.archive_guid)

        if self.site is not None and not isinstance(self.site, SiteSiteCode):
            self.site = SiteSiteCode(self.site)

        if self.location is not None and not isinstance(self.location, LocationLocationName):
            self.location = LocationLocationName(self.location)

        if self.collection_date is not None and not isinstance(self.collection_date, XSDDate):
            self.collection_date = XSDDate(self.collection_date)

        if self.taxon is not None and not isinstance(self.taxon, TaxonTaxonId):
            self.taxon = TaxonTaxonId(self.taxon)

        if not isinstance(self.parent_samples, list):
            self.parent_samples = [self.parent_samples] if self.parent_samples is not None else []
        self.parent_samples = [v if isinstance(v, SampleSampleUuid) else SampleSampleUuid(v) for v in self.parent_samples]

        if not isinstance(self.child_samples, list):
            self.child_samples = [self.child_samples] if self.child_samples is not None else []
        self.child_samples = [v if isinstance(v, SampleSampleUuid) else SampleSampleUuid(v) for v in self.child_samples]

        if self.data_product is not None and not isinstance(self.data_product, DataProductProductCode):
            self.data_product = DataProductProductCode(self.data_product)

        self._normalize_inlined_as_list(slot_name="sample_events", slot_type=SampleEvent, key_name="event_id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SampleEvent(YAMLRoot):
    """
    A custody or processing event for a sample
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NEON["SampleEvent"]
    class_class_curie: ClassVar[str] = "neon:SampleEvent"
    class_name: ClassVar[str] = "SampleEvent"
    class_model_uri: ClassVar[URIRef] = NEON.SampleEvent

    event_id: Union[str, SampleEventEventId] = None
    event_date: Optional[Union[str, XSDDateTime]] = None
    ingest_table_name: Optional[str] = None
    field_entries: Optional[Union[Union[dict, "FieldEntry"], list[Union[dict, "FieldEntry"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.event_id):
            self.MissingRequiredField("event_id")
        if not isinstance(self.event_id, SampleEventEventId):
            self.event_id = SampleEventEventId(self.event_id)

        if self.event_date is not None and not isinstance(self.event_date, XSDDateTime):
            self.event_date = XSDDateTime(self.event_date)

        if self.ingest_table_name is not None and not isinstance(self.ingest_table_name, str):
            self.ingest_table_name = str(self.ingest_table_name)

        self._normalize_inlined_as_list(slot_name="field_entries", slot_type=FieldEntry, key_name="field_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FieldEntry(YAMLRoot):
    """
    A field name/value pair from a sample event
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NEON["FieldEntry"]
    class_class_curie: ClassVar[str] = "neon:FieldEntry"
    class_name: ClassVar[str] = "FieldEntry"
    class_model_uri: ClassVar[URIRef] = NEON.FieldEntry

    field_name: str = None
    field_value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.field_name):
            self.MissingRequiredField("field_name")
        if not isinstance(self.field_name, str):
            self.field_name = str(self.field_name)

        if self.field_value is not None and not isinstance(self.field_value, str):
            self.field_value = str(self.field_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Taxon(YAMLRoot):
    """
    A taxonomic record from NEON's taxon lists, following Darwin Core standards. Taxa are compiled from published
    sources for field staff verification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC["Taxon"]
    class_class_curie: ClassVar[str] = "dwc:Taxon"
    class_name: ClassVar[str] = "Taxon"
    class_model_uri: ClassVar[URIRef] = NEON.Taxon

    taxon_id: Union[str, TaxonTaxonId] = None
    taxon_type: Union[str, "TaxonTypeEnum"] = None
    scientific_name: str = None
    accepted_taxon_id: Optional[str] = None
    scientific_name_authorship: Optional[str] = None
    vernacular_name: Optional[str] = None
    taxon_rank: Optional[str] = None
    kingdom: Optional[str] = None
    phylum: Optional[str] = None
    class_name: Optional[str] = None
    order: Optional[str] = None
    family: Optional[str] = None
    genus: Optional[str] = None
    species: Optional[str] = None
    subspecies: Optional[str] = None
    gbif_rank: Optional[str] = None
    native_status_code: Optional[str] = None
    update_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.taxon_id):
            self.MissingRequiredField("taxon_id")
        if not isinstance(self.taxon_id, TaxonTaxonId):
            self.taxon_id = TaxonTaxonId(self.taxon_id)

        if self._is_empty(self.taxon_type):
            self.MissingRequiredField("taxon_type")
        if not isinstance(self.taxon_type, TaxonTypeEnum):
            self.taxon_type = TaxonTypeEnum(self.taxon_type)

        if self._is_empty(self.scientific_name):
            self.MissingRequiredField("scientific_name")
        if not isinstance(self.scientific_name, str):
            self.scientific_name = str(self.scientific_name)

        if self.accepted_taxon_id is not None and not isinstance(self.accepted_taxon_id, str):
            self.accepted_taxon_id = str(self.accepted_taxon_id)

        if self.scientific_name_authorship is not None and not isinstance(self.scientific_name_authorship, str):
            self.scientific_name_authorship = str(self.scientific_name_authorship)

        if self.vernacular_name is not None and not isinstance(self.vernacular_name, str):
            self.vernacular_name = str(self.vernacular_name)

        if self.taxon_rank is not None and not isinstance(self.taxon_rank, str):
            self.taxon_rank = str(self.taxon_rank)

        if self.kingdom is not None and not isinstance(self.kingdom, str):
            self.kingdom = str(self.kingdom)

        if self.phylum is not None and not isinstance(self.phylum, str):
            self.phylum = str(self.phylum)

        if self.class_name is not None and not isinstance(self.class_name, str):
            self.class_name = str(self.class_name)

        if self.order is not None and not isinstance(self.order, str):
            self.order = str(self.order)

        if self.family is not None and not isinstance(self.family, str):
            self.family = str(self.family)

        if self.genus is not None and not isinstance(self.genus, str):
            self.genus = str(self.genus)

        if self.species is not None and not isinstance(self.species, str):
            self.species = str(self.species)

        if self.subspecies is not None and not isinstance(self.subspecies, str):
            self.subspecies = str(self.subspecies)

        if self.gbif_rank is not None and not isinstance(self.gbif_rank, str):
            self.gbif_rank = str(self.gbif_rank)

        if self.native_status_code is not None and not isinstance(self.native_status_code, str):
            self.native_status_code = str(self.native_status_code)

        if self.update_date is not None and not isinstance(self.update_date, XSDDate):
            self.update_date = XSDDate(self.update_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Observation(YAMLRoot):
    """
    A generic observation or measurement record from NEON. This is a base class for specific observation types.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Observation"]
    class_class_curie: ClassVar[str] = "schema:Observation"
    class_name: ClassVar[str] = "Observation"
    class_model_uri: ClassVar[URIRef] = NEON.Observation

    observation_id: Union[str, ObservationObservationId] = None
    site: Union[str, SiteSiteCode] = None
    data_product: Union[str, DataProductProductCode] = None
    observation_datetime: Union[str, XSDDateTime] = None
    location: Optional[Union[str, LocationLocationName]] = None
    release: Optional[Union[str, ReleaseReleaseTag]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.observation_id):
            self.MissingRequiredField("observation_id")
        if not isinstance(self.observation_id, ObservationObservationId):
            self.observation_id = ObservationObservationId(self.observation_id)

        if self._is_empty(self.site):
            self.MissingRequiredField("site")
        if not isinstance(self.site, SiteSiteCode):
            self.site = SiteSiteCode(self.site)

        if self._is_empty(self.data_product):
            self.MissingRequiredField("data_product")
        if not isinstance(self.data_product, DataProductProductCode):
            self.data_product = DataProductProductCode(self.data_product)

        if self._is_empty(self.observation_datetime):
            self.MissingRequiredField("observation_datetime")
        if not isinstance(self.observation_datetime, XSDDateTime):
            self.observation_datetime = XSDDateTime(self.observation_datetime)

        if self.location is not None and not isinstance(self.location, LocationLocationName):
            self.location = LocationLocationName(self.location)

        if self.release is not None and not isinstance(self.release, ReleaseReleaseTag):
            self.release = ReleaseReleaseTag(self.release)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalObservation(Observation):
    """
    An observation of a biological organism
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NEON["BiologicalObservation"]
    class_class_curie: ClassVar[str] = "neon:BiologicalObservation"
    class_name: ClassVar[str] = "BiologicalObservation"
    class_model_uri: ClassVar[URIRef] = NEON.BiologicalObservation

    observation_id: Union[str, BiologicalObservationObservationId] = None
    site: Union[str, SiteSiteCode] = None
    data_product: Union[str, DataProductProductCode] = None
    observation_datetime: Union[str, XSDDateTime] = None
    taxon: Optional[Union[str, TaxonTaxonId]] = None
    individual_count: Optional[int] = None
    occurrence_status: Optional[str] = None
    sample: Optional[Union[str, SampleSampleUuid]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.observation_id):
            self.MissingRequiredField("observation_id")
        if not isinstance(self.observation_id, BiologicalObservationObservationId):
            self.observation_id = BiologicalObservationObservationId(self.observation_id)

        if self.taxon is not None and not isinstance(self.taxon, TaxonTaxonId):
            self.taxon = TaxonTaxonId(self.taxon)

        if self.individual_count is not None and not isinstance(self.individual_count, int):
            self.individual_count = int(self.individual_count)

        if self.occurrence_status is not None and not isinstance(self.occurrence_status, str):
            self.occurrence_status = str(self.occurrence_status)

        if self.sample is not None and not isinstance(self.sample, SampleSampleUuid):
            self.sample = SampleSampleUuid(self.sample)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnvironmentalObservation(Observation):
    """
    An environmental or instrumental measurement
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NEON["EnvironmentalObservation"]
    class_class_curie: ClassVar[str] = "neon:EnvironmentalObservation"
    class_name: ClassVar[str] = "EnvironmentalObservation"
    class_model_uri: ClassVar[URIRef] = NEON.EnvironmentalObservation

    observation_id: Union[str, EnvironmentalObservationObservationId] = None
    site: Union[str, SiteSiteCode] = None
    data_product: Union[str, DataProductProductCode] = None
    observation_datetime: Union[str, XSDDateTime] = None
    measured_property: str = None
    measurement_value: Optional[Decimal] = None
    measurement_unit: Optional[str] = None
    quality_flag: Optional[str] = None
    sensor_location: Optional[Union[str, LocationLocationName]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.observation_id):
            self.MissingRequiredField("observation_id")
        if not isinstance(self.observation_id, EnvironmentalObservationObservationId):
            self.observation_id = EnvironmentalObservationObservationId(self.observation_id)

        if self._is_empty(self.measured_property):
            self.MissingRequiredField("measured_property")
        if not isinstance(self.measured_property, str):
            self.measured_property = str(self.measured_property)

        if self.measurement_value is not None and not isinstance(self.measurement_value, Decimal):
            self.measurement_value = Decimal(self.measurement_value)

        if self.measurement_unit is not None and not isinstance(self.measurement_unit, str):
            self.measurement_unit = str(self.measurement_unit)

        if self.quality_flag is not None and not isinstance(self.quality_flag, str):
            self.quality_flag = str(self.quality_flag)

        if self.sensor_location is not None and not isinstance(self.sensor_location, LocationLocationName):
            self.sensor_location = LocationLocationName(self.sensor_location)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiorepositoryCollection(YAMLRoot):
    """
    A collection of samples held in a biorepository
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NEON["BiorepositoryCollection"]
    class_class_curie: ClassVar[str] = "neon:BiorepositoryCollection"
    class_name: ClassVar[str] = "BiorepositoryCollection"
    class_model_uri: ClassVar[URIRef] = NEON.BiorepositoryCollection

    collection_code: Union[str, BiorepositoryCollectionCollectionCode] = None
    collection_name: str = None
    collection_url: Optional[Union[str, URI]] = None
    data_products: Optional[Union[Union[str, DataProductProductCode], list[Union[str, DataProductProductCode]]]] = empty_list()
    samples: Optional[Union[Union[str, SampleSampleUuid], list[Union[str, SampleSampleUuid]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.collection_code):
            self.MissingRequiredField("collection_code")
        if not isinstance(self.collection_code, BiorepositoryCollectionCollectionCode):
            self.collection_code = BiorepositoryCollectionCollectionCode(self.collection_code)

        if self._is_empty(self.collection_name):
            self.MissingRequiredField("collection_name")
        if not isinstance(self.collection_name, str):
            self.collection_name = str(self.collection_name)

        if self.collection_url is not None and not isinstance(self.collection_url, URI):
            self.collection_url = URI(self.collection_url)

        if not isinstance(self.data_products, list):
            self.data_products = [self.data_products] if self.data_products is not None else []
        self.data_products = [v if isinstance(v, DataProductProductCode) else DataProductProductCode(v) for v in self.data_products]

        if not isinstance(self.samples, list):
            self.samples = [self.samples] if self.samples is not None else []
        self.samples = [v if isinstance(v, SampleSampleUuid) else SampleSampleUuid(v) for v in self.samples]

        super().__post_init__(**kwargs)


# Enumerations
class SiteTypeEnum(EnumDefinitionImpl):
    """
    Type of NEON field site
    """
    CORE = PermissibleValue(
        text="CORE",
        description="Core sites selected to represent key ecosystem types")
    GRADIENT = PermissibleValue(
        text="GRADIENT",
        description="Gradient sites capturing environmental gradients")

    _defn = EnumDefinition(
        name="SiteTypeEnum",
        description="Type of NEON field site",
    )

class ProductStatusEnum(EnumDefinitionImpl):
    """
    Status of a data product
    """
    FUTURE = PermissibleValue(
        text="FUTURE",
        description="Product planned for future release")
    ACTIVE = PermissibleValue(
        text="ACTIVE",
        description="Product currently being collected and released")
    RETIRED = PermissibleValue(
        text="RETIRED",
        description="Product no longer being collected")

    _defn = EnumDefinition(
        name="ProductStatusEnum",
        description="Status of a data product",
    )

class ProductCategoryEnum(EnumDefinitionImpl):
    """
    Data product processing level
    """
    _defn = EnumDefinition(
        name="ProductCategoryEnum",
        description="Data product processing level",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Level 0",
            PermissibleValue(
                text="Level 0",
                description="Raw data"))
        setattr(cls, "Level 1",
            PermissibleValue(
                text="Level 1",
                description="Quality-controlled data"))
        setattr(cls, "Level 2",
            PermissibleValue(
                text="Level 2",
                description="Derived data products"))
        setattr(cls, "Level 3",
            PermissibleValue(
                text="Level 3",
                description="Highly processed/modeled data"))
        setattr(cls, "Level 4",
            PermissibleValue(
                text="Level 4",
                description="Integrated data products"))

class TaxonTypeEnum(EnumDefinitionImpl):
    """
    Major taxonomic groupings used by NEON
    """
    ALGAE = PermissibleValue(
        text="ALGAE",
        description="Algae taxa")
    BEETLE = PermissibleValue(
        text="BEETLE",
        description="Beetle taxa (Carabidae)")
    BIRD = PermissibleValue(
        text="BIRD",
        description="Bird taxa")
    FISH = PermissibleValue(
        text="FISH",
        description="Fish taxa")
    HERPETOLOGY = PermissibleValue(
        text="HERPETOLOGY",
        description="Reptile and amphibian taxa")
    MACROINVERTEBRATE = PermissibleValue(
        text="MACROINVERTEBRATE",
        description="Aquatic macroinvertebrate taxa")
    MOSQUITO = PermissibleValue(
        text="MOSQUITO",
        description="Mosquito taxa")
    MOSQUITO_PATHOGENS = PermissibleValue(
        text="MOSQUITO_PATHOGENS",
        description="Mosquito pathogen taxa")
    PLANT = PermissibleValue(
        text="PLANT",
        description="Plant taxa")
    SMALL_MAMMAL = PermissibleValue(
        text="SMALL_MAMMAL",
        description="Small mammal taxa")
    TICK = PermissibleValue(
        text="TICK",
        description="Tick taxa")

    _defn = EnumDefinition(
        name="TaxonTypeEnum",
        description="Major taxonomic groupings used by NEON",
    )

class LocationTypeEnum(EnumDefinitionImpl):
    """
    Types of named locations in NEON hierarchy
    """
    REALM = PermissibleValue(
        text="REALM",
        description="Top-level realm")
    DOMAIN = PermissibleValue(
        text="DOMAIN",
        description="Ecological domain")
    SITE = PermissibleValue(
        text="SITE",
        description="Field site")
    TOWER = PermissibleValue(
        text="TOWER",
        description="Instrumented tower")
    PLOT = PermissibleValue(
        text="PLOT",
        description="Sampling plot")
    POINT = PermissibleValue(
        text="POINT",
        description="Observation point")
    SENSOR = PermissibleValue(
        text="SENSOR",
        description="Individual sensor location")

    _defn = EnumDefinition(
        name="LocationTypeEnum",
        description="Types of named locations in NEON hierarchy",
    )

class MeasurementSystemEnum(EnumDefinitionImpl):
    """
    NEON measurement system types
    """
    AOP = PermissibleValue(
        text="AOP",
        description="Airborne Observation Platform")
    AIS = PermissibleValue(
        text="AIS",
        description="Aquatic Instrument System")
    AOS = PermissibleValue(
        text="AOS",
        description="Aquatic Observation System")
    TIS = PermissibleValue(
        text="TIS",
        description="Terrestrial Instrument System")
    TOS = PermissibleValue(
        text="TOS",
        description="Terrestrial Observation System")

    _defn = EnumDefinition(
        name="MeasurementSystemEnum",
        description="NEON measurement system types",
    )

# Slots
class slots:
    pass

slots.neonDataset__domains = Slot(uri=NEON.domains, name="neonDataset__domains", curie=NEON.curie('domains'),
                   model_uri=NEON.neonDataset__domains, domain=None, range=Optional[Union[dict[Union[str, DomainDomainCode], Union[dict, Domain]], list[Union[dict, Domain]]]])

slots.neonDataset__sites = Slot(uri=NEON.sites, name="neonDataset__sites", curie=NEON.curie('sites'),
                   model_uri=NEON.neonDataset__sites, domain=None, range=Optional[Union[dict[Union[str, SiteSiteCode], Union[dict, Site]], list[Union[dict, Site]]]])

slots.neonDataset__locations = Slot(uri=NEON.locations, name="neonDataset__locations", curie=NEON.curie('locations'),
                   model_uri=NEON.neonDataset__locations, domain=None, range=Optional[Union[dict[Union[str, LocationLocationName], Union[dict, Location]], list[Union[dict, Location]]]])

slots.neonDataset__data_products = Slot(uri=NEON.data_products, name="neonDataset__data_products", curie=NEON.curie('data_products'),
                   model_uri=NEON.neonDataset__data_products, domain=None, range=Optional[Union[dict[Union[str, DataProductProductCode], Union[dict, DataProduct]], list[Union[dict, DataProduct]]]])

slots.neonDataset__releases = Slot(uri=NEON.releases, name="neonDataset__releases", curie=NEON.curie('releases'),
                   model_uri=NEON.neonDataset__releases, domain=None, range=Optional[Union[dict[Union[str, ReleaseReleaseTag], Union[dict, Release]], list[Union[dict, Release]]]])

slots.neonDataset__taxa = Slot(uri=NEON.taxa, name="neonDataset__taxa", curie=NEON.curie('taxa'),
                   model_uri=NEON.neonDataset__taxa, domain=None, range=Optional[Union[dict[Union[str, TaxonTaxonId], Union[dict, Taxon]], list[Union[dict, Taxon]]]])

slots.neonDataset__samples = Slot(uri=NEON.samples, name="neonDataset__samples", curie=NEON.curie('samples'),
                   model_uri=NEON.neonDataset__samples, domain=None, range=Optional[Union[dict[Union[str, SampleSampleUuid], Union[dict, Sample]], list[Union[dict, Sample]]]])

slots.domain__domain_code = Slot(uri=DCTERMS.identifier, name="domain__domain_code", curie=DCTERMS.curie('identifier'),
                   model_uri=NEON.domain__domain_code, domain=None, range=URIRef)

slots.domain__domain_name = Slot(uri=SCHEMA.name, name="domain__domain_name", curie=SCHEMA.curie('name'),
                   model_uri=NEON.domain__domain_name, domain=None, range=str)

slots.domain__description = Slot(uri=SCHEMA.description, name="domain__description", curie=SCHEMA.curie('description'),
                   model_uri=NEON.domain__description, domain=None, range=Optional[str])

slots.domain__sites = Slot(uri=NEON.sites, name="domain__sites", curie=NEON.curie('sites'),
                   model_uri=NEON.domain__sites, domain=None, range=Optional[Union[Union[str, SiteSiteCode], list[Union[str, SiteSiteCode]]]])

slots.site__site_code = Slot(uri=DCTERMS.identifier, name="site__site_code", curie=DCTERMS.curie('identifier'),
                   model_uri=NEON.site__site_code, domain=None, range=URIRef)

slots.site__site_name = Slot(uri=SCHEMA.name, name="site__site_name", curie=SCHEMA.curie('name'),
                   model_uri=NEON.site__site_name, domain=None, range=str)

slots.site__site_description = Slot(uri=SCHEMA.description, name="site__site_description", curie=SCHEMA.curie('description'),
                   model_uri=NEON.site__site_description, domain=None, range=Optional[str])

slots.site__site_type = Slot(uri=NEON.site_type, name="site__site_type", curie=NEON.curie('site_type'),
                   model_uri=NEON.site__site_type, domain=None, range=Union[str, "SiteTypeEnum"])

slots.site__domain = Slot(uri=SCHEMA.containedInPlace, name="site__domain", curie=SCHEMA.curie('containedInPlace'),
                   model_uri=NEON.site__domain, domain=None, range=Union[str, DomainDomainCode])

slots.site__latitude = Slot(uri=WGS84.lat, name="site__latitude", curie=WGS84.curie('lat'),
                   model_uri=NEON.site__latitude, domain=None, range=Optional[Decimal])

slots.site__longitude = Slot(uri=WGS84.long, name="site__longitude", curie=WGS84.curie('long'),
                   model_uri=NEON.site__longitude, domain=None, range=Optional[Decimal])

slots.site__elevation = Slot(uri=NEON.elevation, name="site__elevation", curie=NEON.curie('elevation'),
                   model_uri=NEON.site__elevation, domain=None, range=Optional[Decimal])

slots.site__state_code = Slot(uri=NEON.state_code, name="site__state_code", curie=NEON.curie('state_code'),
                   model_uri=NEON.site__state_code, domain=None, range=Optional[str])

slots.site__state_name = Slot(uri=NEON.state_name, name="site__state_name", curie=NEON.curie('state_name'),
                   model_uri=NEON.site__state_name, domain=None, range=Optional[str])

slots.site__deims_id = Slot(uri=NEON.deims_id, name="site__deims_id", curie=NEON.curie('deims_id'),
                   model_uri=NEON.site__deims_id, domain=None, range=Optional[str])

slots.site__available_data_products = Slot(uri=NEON.available_data_products, name="site__available_data_products", curie=NEON.curie('available_data_products'),
                   model_uri=NEON.site__available_data_products, domain=None, range=Optional[Union[Union[str, DataProductProductCode], list[Union[str, DataProductProductCode]]]])

slots.site__locations = Slot(uri=NEON.locations, name="site__locations", curie=NEON.curie('locations'),
                   model_uri=NEON.site__locations, domain=None, range=Optional[Union[Union[str, LocationLocationName], list[Union[str, LocationLocationName]]]])

slots.location__location_name = Slot(uri=DCTERMS.identifier, name="location__location_name", curie=DCTERMS.curie('identifier'),
                   model_uri=NEON.location__location_name, domain=None, range=URIRef)

slots.location__location_description = Slot(uri=SCHEMA.description, name="location__location_description", curie=SCHEMA.curie('description'),
                   model_uri=NEON.location__location_description, domain=None, range=Optional[str])

slots.location__location_type = Slot(uri=NEON.location_type, name="location__location_type", curie=NEON.curie('location_type'),
                   model_uri=NEON.location__location_type, domain=None, range=Optional[Union[str, "LocationTypeEnum"]])

slots.location__site = Slot(uri=SCHEMA.containedInPlace, name="location__site", curie=SCHEMA.curie('containedInPlace'),
                   model_uri=NEON.location__site, domain=None, range=Optional[Union[str, SiteSiteCode]])

slots.location__parent_location = Slot(uri=NEON.parent_location, name="location__parent_location", curie=NEON.curie('parent_location'),
                   model_uri=NEON.location__parent_location, domain=None, range=Optional[Union[str, LocationLocationName]])

slots.location__child_locations = Slot(uri=NEON.child_locations, name="location__child_locations", curie=NEON.curie('child_locations'),
                   model_uri=NEON.location__child_locations, domain=None, range=Optional[Union[Union[str, LocationLocationName], list[Union[str, LocationLocationName]]]])

slots.location__latitude = Slot(uri=WGS84.lat, name="location__latitude", curie=WGS84.curie('lat'),
                   model_uri=NEON.location__latitude, domain=None, range=Optional[Decimal])

slots.location__longitude = Slot(uri=WGS84.long, name="location__longitude", curie=WGS84.curie('long'),
                   model_uri=NEON.location__longitude, domain=None, range=Optional[Decimal])

slots.location__elevation = Slot(uri=NEON.elevation, name="location__elevation", curie=NEON.curie('elevation'),
                   model_uri=NEON.location__elevation, domain=None, range=Optional[Decimal])

slots.location__utm_easting = Slot(uri=NEON.utm_easting, name="location__utm_easting", curie=NEON.curie('utm_easting'),
                   model_uri=NEON.location__utm_easting, domain=None, range=Optional[Decimal])

slots.location__utm_northing = Slot(uri=NEON.utm_northing, name="location__utm_northing", curie=NEON.curie('utm_northing'),
                   model_uri=NEON.location__utm_northing, domain=None, range=Optional[Decimal])

slots.location__utm_zone = Slot(uri=NEON.utm_zone, name="location__utm_zone", curie=NEON.curie('utm_zone'),
                   model_uri=NEON.location__utm_zone, domain=None, range=Optional[int])

slots.location__active_periods = Slot(uri=NEON.active_periods, name="location__active_periods", curie=NEON.curie('active_periods'),
                   model_uri=NEON.location__active_periods, domain=None, range=Optional[Union[Union[dict, TimePeriod], list[Union[dict, TimePeriod]]]])

slots.timePeriod__start_date = Slot(uri=SCHEMA.startDate, name="timePeriod__start_date", curie=SCHEMA.curie('startDate'),
                   model_uri=NEON.timePeriod__start_date, domain=None, range=Union[str, XSDDate])

slots.timePeriod__end_date = Slot(uri=SCHEMA.endDate, name="timePeriod__end_date", curie=SCHEMA.curie('endDate'),
                   model_uri=NEON.timePeriod__end_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.geoCoordinates__latitude = Slot(uri=WGS84.lat, name="geoCoordinates__latitude", curie=WGS84.curie('lat'),
                   model_uri=NEON.geoCoordinates__latitude, domain=None, range=Optional[Decimal])

slots.geoCoordinates__longitude = Slot(uri=WGS84.long, name="geoCoordinates__longitude", curie=WGS84.curie('long'),
                   model_uri=NEON.geoCoordinates__longitude, domain=None, range=Optional[Decimal])

slots.geoCoordinates__elevation = Slot(uri=NEON.elevation, name="geoCoordinates__elevation", curie=NEON.curie('elevation'),
                   model_uri=NEON.geoCoordinates__elevation, domain=None, range=Optional[Decimal])

slots.dataProduct__product_code = Slot(uri=DCTERMS.identifier, name="dataProduct__product_code", curie=DCTERMS.curie('identifier'),
                   model_uri=NEON.dataProduct__product_code, domain=None, range=URIRef)

slots.dataProduct__product_name = Slot(uri=SCHEMA.name, name="dataProduct__product_name", curie=SCHEMA.curie('name'),
                   model_uri=NEON.dataProduct__product_name, domain=None, range=str)

slots.dataProduct__product_description = Slot(uri=SCHEMA.description, name="dataProduct__product_description", curie=SCHEMA.curie('description'),
                   model_uri=NEON.dataProduct__product_description, domain=None, range=Optional[str])

slots.dataProduct__product_abstract = Slot(uri=NEON.product_abstract, name="dataProduct__product_abstract", curie=NEON.curie('product_abstract'),
                   model_uri=NEON.dataProduct__product_abstract, domain=None, range=Optional[str])

slots.dataProduct__product_status = Slot(uri=NEON.product_status, name="dataProduct__product_status", curie=NEON.curie('product_status'),
                   model_uri=NEON.dataProduct__product_status, domain=None, range=Optional[Union[str, "ProductStatusEnum"]])

slots.dataProduct__product_category = Slot(uri=NEON.product_category, name="dataProduct__product_category", curie=NEON.curie('product_category'),
                   model_uri=NEON.dataProduct__product_category, domain=None, range=Optional[Union[str, "ProductCategoryEnum"]])

slots.dataProduct__product_has_expanded = Slot(uri=NEON.product_has_expanded, name="dataProduct__product_has_expanded", curie=NEON.curie('product_has_expanded'),
                   model_uri=NEON.dataProduct__product_has_expanded, domain=None, range=Optional[Union[bool, Bool]])

slots.dataProduct__science_team = Slot(uri=NEON.science_team, name="dataProduct__science_team", curie=NEON.curie('science_team'),
                   model_uri=NEON.dataProduct__science_team, domain=None, range=Optional[str])

slots.dataProduct__measurement_system = Slot(uri=NEON.measurement_system, name="dataProduct__measurement_system", curie=NEON.curie('measurement_system'),
                   model_uri=NEON.dataProduct__measurement_system, domain=None, range=Optional[Union[str, "MeasurementSystemEnum"]])

slots.dataProduct__sites = Slot(uri=NEON.sites, name="dataProduct__sites", curie=NEON.curie('sites'),
                   model_uri=NEON.dataProduct__sites, domain=None, range=Optional[Union[Union[dict, SiteAvailability], list[Union[dict, SiteAvailability]]]])

slots.dataProduct__releases = Slot(uri=NEON.releases, name="dataProduct__releases", curie=NEON.curie('releases'),
                   model_uri=NEON.dataProduct__releases, domain=None, range=Optional[Union[Union[str, ReleaseReleaseTag], list[Union[str, ReleaseReleaseTag]]]])

slots.dataProduct__specifications = Slot(uri=NEON.specifications, name="dataProduct__specifications", curie=NEON.curie('specifications'),
                   model_uri=NEON.dataProduct__specifications, domain=None, range=Optional[Union[dict[Union[str, ProductSpecificationSpecId], Union[dict, ProductSpecification]], list[Union[dict, ProductSpecification]]]])

slots.dataProduct__change_logs = Slot(uri=NEON.change_logs, name="dataProduct__change_logs", curie=NEON.curie('change_logs'),
                   model_uri=NEON.dataProduct__change_logs, domain=None, range=Optional[Union[dict[Union[str, ChangeLogEntryIssueId], Union[dict, ChangeLogEntry]], list[Union[dict, ChangeLogEntry]]]])

slots.dataProduct__keywords = Slot(uri=SCHEMA.keywords, name="dataProduct__keywords", curie=SCHEMA.curie('keywords'),
                   model_uri=NEON.dataProduct__keywords, domain=None, range=Optional[Union[str, list[str]]])

slots.siteAvailability__site = Slot(uri=NEON.site, name="siteAvailability__site", curie=NEON.curie('site'),
                   model_uri=NEON.siteAvailability__site, domain=None, range=Union[str, SiteSiteCode])

slots.siteAvailability__available_months = Slot(uri=NEON.available_months, name="siteAvailability__available_months", curie=NEON.curie('available_months'),
                   model_uri=NEON.siteAvailability__available_months, domain=None, range=Optional[Union[Union[str, YearMonth], list[Union[str, YearMonth]]]])

slots.siteAvailability__data_url = Slot(uri=SCHEMA.url, name="siteAvailability__data_url", curie=SCHEMA.curie('url'),
                   model_uri=NEON.siteAvailability__data_url, domain=None, range=Optional[Union[str, URI]])

slots.productSpecification__spec_id = Slot(uri=NEON.spec_id, name="productSpecification__spec_id", curie=NEON.curie('spec_id'),
                   model_uri=NEON.productSpecification__spec_id, domain=None, range=URIRef)

slots.productSpecification__spec_description = Slot(uri=NEON.spec_description, name="productSpecification__spec_description", curie=NEON.curie('spec_description'),
                   model_uri=NEON.productSpecification__spec_description, domain=None, range=Optional[str])

slots.productSpecification__spec_type = Slot(uri=NEON.spec_type, name="productSpecification__spec_type", curie=NEON.curie('spec_type'),
                   model_uri=NEON.productSpecification__spec_type, domain=None, range=Optional[str])

slots.productSpecification__file_name = Slot(uri=NEON.file_name, name="productSpecification__file_name", curie=NEON.curie('file_name'),
                   model_uri=NEON.productSpecification__file_name, domain=None, range=Optional[str])

slots.productSpecification__file_size = Slot(uri=NEON.file_size, name="productSpecification__file_size", curie=NEON.curie('file_size'),
                   model_uri=NEON.productSpecification__file_size, domain=None, range=Optional[int])

slots.productSpecification__mime_type = Slot(uri=NEON.mime_type, name="productSpecification__mime_type", curie=NEON.curie('mime_type'),
                   model_uri=NEON.productSpecification__mime_type, domain=None, range=Optional[str])

slots.productSpecification__url = Slot(uri=SCHEMA.url, name="productSpecification__url", curie=SCHEMA.curie('url'),
                   model_uri=NEON.productSpecification__url, domain=None, range=Optional[Union[str, URI]])

slots.changeLogEntry__issue_id = Slot(uri=NEON.issue_id, name="changeLogEntry__issue_id", curie=NEON.curie('issue_id'),
                   model_uri=NEON.changeLogEntry__issue_id, domain=None, range=URIRef)

slots.changeLogEntry__parent_issue_id = Slot(uri=NEON.parent_issue_id, name="changeLogEntry__parent_issue_id", curie=NEON.curie('parent_issue_id'),
                   model_uri=NEON.changeLogEntry__parent_issue_id, domain=None, range=Optional[str])

slots.changeLogEntry__issue = Slot(uri=NEON.issue, name="changeLogEntry__issue", curie=NEON.curie('issue'),
                   model_uri=NEON.changeLogEntry__issue, domain=None, range=str)

slots.changeLogEntry__resolution = Slot(uri=NEON.resolution, name="changeLogEntry__resolution", curie=NEON.curie('resolution'),
                   model_uri=NEON.changeLogEntry__resolution, domain=None, range=Optional[str])

slots.changeLogEntry__date_range_start = Slot(uri=SCHEMA.startDate, name="changeLogEntry__date_range_start", curie=SCHEMA.curie('startDate'),
                   model_uri=NEON.changeLogEntry__date_range_start, domain=None, range=Optional[Union[str, XSDDate]])

slots.changeLogEntry__date_range_end = Slot(uri=SCHEMA.endDate, name="changeLogEntry__date_range_end", curie=SCHEMA.curie('endDate'),
                   model_uri=NEON.changeLogEntry__date_range_end, domain=None, range=Optional[Union[str, XSDDate]])

slots.changeLogEntry__locations_affected = Slot(uri=NEON.locations_affected, name="changeLogEntry__locations_affected", curie=NEON.curie('locations_affected'),
                   model_uri=NEON.changeLogEntry__locations_affected, domain=None, range=Optional[Union[Union[str, LocationLocationName], list[Union[str, LocationLocationName]]]])

slots.changeLogEntry__created_date = Slot(uri=NEON.created_date, name="changeLogEntry__created_date", curie=NEON.curie('created_date'),
                   model_uri=NEON.changeLogEntry__created_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.changeLogEntry__resolved_date = Slot(uri=NEON.resolved_date, name="changeLogEntry__resolved_date", curie=NEON.curie('resolved_date'),
                   model_uri=NEON.changeLogEntry__resolved_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.release__release_tag = Slot(uri=DCTERMS.identifier, name="release__release_tag", curie=DCTERMS.curie('identifier'),
                   model_uri=NEON.release__release_tag, domain=None, range=URIRef)

slots.release__uuid = Slot(uri=NEON.uuid, name="release__uuid", curie=NEON.curie('uuid'),
                   model_uri=NEON.release__uuid, domain=None, range=Optional[str])

slots.release__generation_date = Slot(uri=SCHEMA.datePublished, name="release__generation_date", curie=SCHEMA.curie('datePublished'),
                   model_uri=NEON.release__generation_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.release__doi = Slot(uri=DCTERMS.identifier, name="release__doi", curie=DCTERMS.curie('identifier'),
                   model_uri=NEON.release__doi, domain=None, range=Optional[str])

slots.release__data_products = Slot(uri=NEON.data_products, name="release__data_products", curie=NEON.curie('data_products'),
                   model_uri=NEON.release__data_products, domain=None, range=Optional[Union[Union[str, DataProductProductCode], list[Union[str, DataProductProductCode]]]])

slots.release__artifacts = Slot(uri=NEON.artifacts, name="release__artifacts", curie=NEON.curie('artifacts'),
                   model_uri=NEON.release__artifacts, domain=None, range=Optional[Union[Union[dict, ReleaseArtifact], list[Union[dict, ReleaseArtifact]]]])

slots.release__description = Slot(uri=SCHEMA.description, name="release__description", curie=SCHEMA.curie('description'),
                   model_uri=NEON.release__description, domain=None, range=Optional[str])

slots.releaseArtifact__name = Slot(uri=SCHEMA.name, name="releaseArtifact__name", curie=SCHEMA.curie('name'),
                   model_uri=NEON.releaseArtifact__name, domain=None, range=str)

slots.releaseArtifact__artifact_type = Slot(uri=NEON.artifact_type, name="releaseArtifact__artifact_type", curie=NEON.curie('artifact_type'),
                   model_uri=NEON.releaseArtifact__artifact_type, domain=None, range=Optional[str])

slots.releaseArtifact__file_size = Slot(uri=NEON.file_size, name="releaseArtifact__file_size", curie=NEON.curie('file_size'),
                   model_uri=NEON.releaseArtifact__file_size, domain=None, range=Optional[int])

slots.releaseArtifact__md5_checksum = Slot(uri=NEON.md5_checksum, name="releaseArtifact__md5_checksum", curie=NEON.curie('md5_checksum'),
                   model_uri=NEON.releaseArtifact__md5_checksum, domain=None, range=Optional[str])

slots.releaseArtifact__url = Slot(uri=SCHEMA.url, name="releaseArtifact__url", curie=SCHEMA.curie('url'),
                   model_uri=NEON.releaseArtifact__url, domain=None, range=Optional[Union[str, URI]])

slots.dataFile__file_name = Slot(uri=SCHEMA.name, name="dataFile__file_name", curie=SCHEMA.curie('name'),
                   model_uri=NEON.dataFile__file_name, domain=None, range=URIRef)

slots.dataFile__data_product = Slot(uri=NEON.data_product, name="dataFile__data_product", curie=NEON.curie('data_product'),
                   model_uri=NEON.dataFile__data_product, domain=None, range=Union[str, DataProductProductCode])

slots.dataFile__site = Slot(uri=NEON.site, name="dataFile__site", curie=NEON.curie('site'),
                   model_uri=NEON.dataFile__site, domain=None, range=Union[str, SiteSiteCode])

slots.dataFile__year_month = Slot(uri=NEON.year_month, name="dataFile__year_month", curie=NEON.curie('year_month'),
                   model_uri=NEON.dataFile__year_month, domain=None, range=Union[str, YearMonth])

slots.dataFile__release = Slot(uri=NEON.release, name="dataFile__release", curie=NEON.curie('release'),
                   model_uri=NEON.dataFile__release, domain=None, range=Optional[Union[str, ReleaseReleaseTag]])

slots.dataFile__file_size = Slot(uri=NEON.file_size, name="dataFile__file_size", curie=NEON.curie('file_size'),
                   model_uri=NEON.dataFile__file_size, domain=None, range=Optional[int])

slots.dataFile__url = Slot(uri=SCHEMA.url, name="dataFile__url", curie=SCHEMA.curie('url'),
                   model_uri=NEON.dataFile__url, domain=None, range=Optional[Union[str, URI]])

slots.dataFile__md5_checksum = Slot(uri=NEON.md5_checksum, name="dataFile__md5_checksum", curie=NEON.curie('md5_checksum'),
                   model_uri=NEON.dataFile__md5_checksum, domain=None, range=Optional[str])

slots.dataFile__crc32_checksum = Slot(uri=NEON.crc32_checksum, name="dataFile__crc32_checksum", curie=NEON.curie('crc32_checksum'),
                   model_uri=NEON.dataFile__crc32_checksum, domain=None, range=Optional[str])

slots.dataFile__crc32c_checksum = Slot(uri=NEON.crc32c_checksum, name="dataFile__crc32c_checksum", curie=NEON.curie('crc32c_checksum'),
                   model_uri=NEON.dataFile__crc32c_checksum, domain=None, range=Optional[str])

slots.dataFile__package_type = Slot(uri=NEON.package_type, name="dataFile__package_type", curie=NEON.curie('package_type'),
                   model_uri=NEON.dataFile__package_type, domain=None, range=Optional[str])

slots.sample__sample_uuid = Slot(uri=DWC.materialSampleID, name="sample__sample_uuid", curie=DWC.curie('materialSampleID'),
                   model_uri=NEON.sample__sample_uuid, domain=None, range=URIRef)

slots.sample__sample_tag = Slot(uri=NEON.sample_tag, name="sample__sample_tag", curie=NEON.curie('sample_tag'),
                   model_uri=NEON.sample__sample_tag, domain=None, range=Optional[str])

slots.sample__sample_class = Slot(uri=NEON.sample_class, name="sample__sample_class", curie=NEON.curie('sample_class'),
                   model_uri=NEON.sample__sample_class, domain=None, range=Optional[str])

slots.sample__barcode = Slot(uri=NEON.barcode, name="sample__barcode", curie=NEON.curie('barcode'),
                   model_uri=NEON.sample__barcode, domain=None, range=Optional[str])

slots.sample__archive_guid = Slot(uri=NEON.archive_guid, name="sample__archive_guid", curie=NEON.curie('archive_guid'),
                   model_uri=NEON.sample__archive_guid, domain=None, range=Optional[str])

slots.sample__site = Slot(uri=DWC.locationID, name="sample__site", curie=DWC.curie('locationID'),
                   model_uri=NEON.sample__site, domain=None, range=Optional[Union[str, SiteSiteCode]])

slots.sample__location = Slot(uri=NEON.location, name="sample__location", curie=NEON.curie('location'),
                   model_uri=NEON.sample__location, domain=None, range=Optional[Union[str, LocationLocationName]])

slots.sample__collection_date = Slot(uri=DWC.eventDate, name="sample__collection_date", curie=DWC.curie('eventDate'),
                   model_uri=NEON.sample__collection_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.sample__taxon = Slot(uri=DWC.taxonID, name="sample__taxon", curie=DWC.curie('taxonID'),
                   model_uri=NEON.sample__taxon, domain=None, range=Optional[Union[str, TaxonTaxonId]])

slots.sample__parent_samples = Slot(uri=NEON.parent_samples, name="sample__parent_samples", curie=NEON.curie('parent_samples'),
                   model_uri=NEON.sample__parent_samples, domain=None, range=Optional[Union[Union[str, SampleSampleUuid], list[Union[str, SampleSampleUuid]]]])

slots.sample__child_samples = Slot(uri=NEON.child_samples, name="sample__child_samples", curie=NEON.curie('child_samples'),
                   model_uri=NEON.sample__child_samples, domain=None, range=Optional[Union[Union[str, SampleSampleUuid], list[Union[str, SampleSampleUuid]]]])

slots.sample__data_product = Slot(uri=NEON.data_product, name="sample__data_product", curie=NEON.curie('data_product'),
                   model_uri=NEON.sample__data_product, domain=None, range=Optional[Union[str, DataProductProductCode]])

slots.sample__sample_events = Slot(uri=NEON.sample_events, name="sample__sample_events", curie=NEON.curie('sample_events'),
                   model_uri=NEON.sample__sample_events, domain=None, range=Optional[Union[dict[Union[str, SampleEventEventId], Union[dict, SampleEvent]], list[Union[dict, SampleEvent]]]])

slots.sampleEvent__event_id = Slot(uri=NEON.event_id, name="sampleEvent__event_id", curie=NEON.curie('event_id'),
                   model_uri=NEON.sampleEvent__event_id, domain=None, range=URIRef)

slots.sampleEvent__event_date = Slot(uri=SCHEMA.startDate, name="sampleEvent__event_date", curie=SCHEMA.curie('startDate'),
                   model_uri=NEON.sampleEvent__event_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.sampleEvent__ingest_table_name = Slot(uri=NEON.ingest_table_name, name="sampleEvent__ingest_table_name", curie=NEON.curie('ingest_table_name'),
                   model_uri=NEON.sampleEvent__ingest_table_name, domain=None, range=Optional[str])

slots.sampleEvent__field_entries = Slot(uri=NEON.field_entries, name="sampleEvent__field_entries", curie=NEON.curie('field_entries'),
                   model_uri=NEON.sampleEvent__field_entries, domain=None, range=Optional[Union[Union[dict, FieldEntry], list[Union[dict, FieldEntry]]]])

slots.fieldEntry__field_name = Slot(uri=NEON.field_name, name="fieldEntry__field_name", curie=NEON.curie('field_name'),
                   model_uri=NEON.fieldEntry__field_name, domain=None, range=str)

slots.fieldEntry__field_value = Slot(uri=NEON.field_value, name="fieldEntry__field_value", curie=NEON.curie('field_value'),
                   model_uri=NEON.fieldEntry__field_value, domain=None, range=Optional[str])

slots.taxon__taxon_id = Slot(uri=DWC.taxonID, name="taxon__taxon_id", curie=DWC.curie('taxonID'),
                   model_uri=NEON.taxon__taxon_id, domain=None, range=URIRef)

slots.taxon__accepted_taxon_id = Slot(uri=DWC.acceptedNameUsageID, name="taxon__accepted_taxon_id", curie=DWC.curie('acceptedNameUsageID'),
                   model_uri=NEON.taxon__accepted_taxon_id, domain=None, range=Optional[str])

slots.taxon__taxon_type = Slot(uri=NEON.taxon_type, name="taxon__taxon_type", curie=NEON.curie('taxon_type'),
                   model_uri=NEON.taxon__taxon_type, domain=None, range=Union[str, "TaxonTypeEnum"])

slots.taxon__scientific_name = Slot(uri=DWC.scientificName, name="taxon__scientific_name", curie=DWC.curie('scientificName'),
                   model_uri=NEON.taxon__scientific_name, domain=None, range=str)

slots.taxon__scientific_name_authorship = Slot(uri=DWC.scientificNameAuthorship, name="taxon__scientific_name_authorship", curie=DWC.curie('scientificNameAuthorship'),
                   model_uri=NEON.taxon__scientific_name_authorship, domain=None, range=Optional[str])

slots.taxon__vernacular_name = Slot(uri=DWC.vernacularName, name="taxon__vernacular_name", curie=DWC.curie('vernacularName'),
                   model_uri=NEON.taxon__vernacular_name, domain=None, range=Optional[str])

slots.taxon__taxon_rank = Slot(uri=DWC.taxonRank, name="taxon__taxon_rank", curie=DWC.curie('taxonRank'),
                   model_uri=NEON.taxon__taxon_rank, domain=None, range=Optional[str])

slots.taxon__kingdom = Slot(uri=DWC.kingdom, name="taxon__kingdom", curie=DWC.curie('kingdom'),
                   model_uri=NEON.taxon__kingdom, domain=None, range=Optional[str])

slots.taxon__phylum = Slot(uri=DWC.phylum, name="taxon__phylum", curie=DWC.curie('phylum'),
                   model_uri=NEON.taxon__phylum, domain=None, range=Optional[str])

slots.taxon__class_name = Slot(uri=DWC.class, name="taxon__class_name", curie=DWC.curie('class'),
                   model_uri=NEON.taxon__class_name, domain=None, range=Optional[str])

slots.taxon__order = Slot(uri=DWC.order, name="taxon__order", curie=DWC.curie('order'),
                   model_uri=NEON.taxon__order, domain=None, range=Optional[str])

slots.taxon__family = Slot(uri=DWC.family, name="taxon__family", curie=DWC.curie('family'),
                   model_uri=NEON.taxon__family, domain=None, range=Optional[str])

slots.taxon__genus = Slot(uri=DWC.genus, name="taxon__genus", curie=DWC.curie('genus'),
                   model_uri=NEON.taxon__genus, domain=None, range=Optional[str])

slots.taxon__species = Slot(uri=DWC.specificEpithet, name="taxon__species", curie=DWC.curie('specificEpithet'),
                   model_uri=NEON.taxon__species, domain=None, range=Optional[str])

slots.taxon__subspecies = Slot(uri=DWC.infraspecificEpithet, name="taxon__subspecies", curie=DWC.curie('infraspecificEpithet'),
                   model_uri=NEON.taxon__subspecies, domain=None, range=Optional[str])

slots.taxon__gbif_rank = Slot(uri=NEON.gbif_rank, name="taxon__gbif_rank", curie=NEON.curie('gbif_rank'),
                   model_uri=NEON.taxon__gbif_rank, domain=None, range=Optional[str])

slots.taxon__native_status_code = Slot(uri=NEON.native_status_code, name="taxon__native_status_code", curie=NEON.curie('native_status_code'),
                   model_uri=NEON.taxon__native_status_code, domain=None, range=Optional[str])

slots.taxon__update_date = Slot(uri=DCTERMS.modified, name="taxon__update_date", curie=DCTERMS.curie('modified'),
                   model_uri=NEON.taxon__update_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.observation__observation_id = Slot(uri=DCTERMS.identifier, name="observation__observation_id", curie=DCTERMS.curie('identifier'),
                   model_uri=NEON.observation__observation_id, domain=None, range=URIRef)

slots.observation__site = Slot(uri=DWC.locationID, name="observation__site", curie=DWC.curie('locationID'),
                   model_uri=NEON.observation__site, domain=None, range=Union[str, SiteSiteCode])

slots.observation__location = Slot(uri=NEON.location, name="observation__location", curie=NEON.curie('location'),
                   model_uri=NEON.observation__location, domain=None, range=Optional[Union[str, LocationLocationName]])

slots.observation__data_product = Slot(uri=NEON.data_product, name="observation__data_product", curie=NEON.curie('data_product'),
                   model_uri=NEON.observation__data_product, domain=None, range=Union[str, DataProductProductCode])

slots.observation__observation_datetime = Slot(uri=DWC.eventDate, name="observation__observation_datetime", curie=DWC.curie('eventDate'),
                   model_uri=NEON.observation__observation_datetime, domain=None, range=Union[str, XSDDateTime])

slots.observation__release = Slot(uri=NEON.release, name="observation__release", curie=NEON.curie('release'),
                   model_uri=NEON.observation__release, domain=None, range=Optional[Union[str, ReleaseReleaseTag]])

slots.biologicalObservation__taxon = Slot(uri=DWC.taxonID, name="biologicalObservation__taxon", curie=DWC.curie('taxonID'),
                   model_uri=NEON.biologicalObservation__taxon, domain=None, range=Optional[Union[str, TaxonTaxonId]])

slots.biologicalObservation__individual_count = Slot(uri=DWC.individualCount, name="biologicalObservation__individual_count", curie=DWC.curie('individualCount'),
                   model_uri=NEON.biologicalObservation__individual_count, domain=None, range=Optional[int])

slots.biologicalObservation__occurrence_status = Slot(uri=DWC.occurrenceStatus, name="biologicalObservation__occurrence_status", curie=DWC.curie('occurrenceStatus'),
                   model_uri=NEON.biologicalObservation__occurrence_status, domain=None, range=Optional[str])

slots.biologicalObservation__sample = Slot(uri=NEON.sample, name="biologicalObservation__sample", curie=NEON.curie('sample'),
                   model_uri=NEON.biologicalObservation__sample, domain=None, range=Optional[Union[str, SampleSampleUuid]])

slots.environmentalObservation__measured_property = Slot(uri=NEON.measured_property, name="environmentalObservation__measured_property", curie=NEON.curie('measured_property'),
                   model_uri=NEON.environmentalObservation__measured_property, domain=None, range=str)

slots.environmentalObservation__measurement_value = Slot(uri=NEON.measurement_value, name="environmentalObservation__measurement_value", curie=NEON.curie('measurement_value'),
                   model_uri=NEON.environmentalObservation__measurement_value, domain=None, range=Optional[Decimal])

slots.environmentalObservation__measurement_unit = Slot(uri=NEON.measurement_unit, name="environmentalObservation__measurement_unit", curie=NEON.curie('measurement_unit'),
                   model_uri=NEON.environmentalObservation__measurement_unit, domain=None, range=Optional[str])

slots.environmentalObservation__quality_flag = Slot(uri=NEON.quality_flag, name="environmentalObservation__quality_flag", curie=NEON.curie('quality_flag'),
                   model_uri=NEON.environmentalObservation__quality_flag, domain=None, range=Optional[str])

slots.environmentalObservation__sensor_location = Slot(uri=NEON.sensor_location, name="environmentalObservation__sensor_location", curie=NEON.curie('sensor_location'),
                   model_uri=NEON.environmentalObservation__sensor_location, domain=None, range=Optional[Union[str, LocationLocationName]])

slots.biorepositoryCollection__collection_code = Slot(uri=DCTERMS.identifier, name="biorepositoryCollection__collection_code", curie=DCTERMS.curie('identifier'),
                   model_uri=NEON.biorepositoryCollection__collection_code, domain=None, range=URIRef)

slots.biorepositoryCollection__collection_name = Slot(uri=SCHEMA.name, name="biorepositoryCollection__collection_name", curie=SCHEMA.curie('name'),
                   model_uri=NEON.biorepositoryCollection__collection_name, domain=None, range=str)

slots.biorepositoryCollection__collection_url = Slot(uri=SCHEMA.url, name="biorepositoryCollection__collection_url", curie=SCHEMA.curie('url'),
                   model_uri=NEON.biorepositoryCollection__collection_url, domain=None, range=Optional[Union[str, URI]])

slots.biorepositoryCollection__data_products = Slot(uri=NEON.data_products, name="biorepositoryCollection__data_products", curie=NEON.curie('data_products'),
                   model_uri=NEON.biorepositoryCollection__data_products, domain=None, range=Optional[Union[Union[str, DataProductProductCode], list[Union[str, DataProductProductCode]]]])

slots.biorepositoryCollection__samples = Slot(uri=NEON.samples, name="biorepositoryCollection__samples", curie=NEON.curie('samples'),
                   model_uri=NEON.biorepositoryCollection__samples, domain=None, range=Optional[Union[Union[str, SampleSampleUuid], list[Union[str, SampleSampleUuid]]]])

