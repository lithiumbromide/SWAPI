---
title: "GetCriteria Method (IPDMWSearchCriteria)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWSearchCriteria"
member: "GetCriteria"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~GetCriteria.html"
---

# GetCriteria Method (IPDMWSearchCriteria)

Gets a search criteria.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCriteria( _
   ByVal Index As System.Integer, _
   ByRef andOr As PDMWAndOr, _
   ByRef propertyType As PDMWPropertyType, _
   ByRef propertyName As System.String, _
   ByRef condition As PDMWConditionType, _
   ByRef Value As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWSearchCriteria
Dim Index As System.Integer
Dim andOr As PDMWAndOr
Dim propertyType As PDMWPropertyType
Dim propertyName As System.String
Dim condition As PDMWConditionType
Dim Value As System.String
Dim value As System.Boolean

value = instance.GetCriteria(Index, andOr, propertyType, propertyName, condition, Value)
```

### C#

```csharp
System.bool GetCriteria(
   System.int Index,
   out PDMWAndOr andOr,
   out PDMWPropertyType propertyType,
   out System.string propertyName,
   out PDMWConditionType condition,
   out System.string Value
)
```

### C++/CLI

```cpp
System.bool GetCriteria(
   System.int Index,
   [Out] PDMWAndOr andOr,
   [Out] PDMWPropertyType propertyType,
   [Out] System.String^ propertyName,
   [Out] PDMWConditionType condition,
   [Out] System.String^ Value
)
```

### Parameters

- `Index`: Index number of the search criteria to get
- `andOr`: Logical operator for subsequent criteria as defined in [PDMWAndOr](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.PDMWAndOr.html)
- `propertyType`: Property type as defined in [PDMWPropertyType](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.PDMWPropertyType.html)
- `propertyName`: Name of property to use with which to search
- `condition`: Search condition as defined in [PDMWConditionType](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.PDMWConditionType.html)
- `Value`: Value of the property for which to search

### Return Value

True if this search criteria is retrieved, false if not

## VBA Syntax

See [PDMWSearchCriteria::GetCriteria](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWSearchCriteria~GetCriteria.html).

## Remarks

To determine the number of search criteria, use [IPDMWSearchCriteria::CriteriaCount](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~CriteriaCount.html) before using this method.

## See Also

[IPDMWSearchCriteria Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria.html)
[IPDMWSearchCriteria Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria_members.html)
[IPDMWSearchCriteria::AddCriteria Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~AddCriteria.html)
[IPDMWSearchCriteria::LoadFromFile Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~LoadFromFile.html)
[IPDMWSearchCriteria::RemoveCriteria Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~RemoveCriteria.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
