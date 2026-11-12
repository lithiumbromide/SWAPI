---
title: "AddCriteria Method (IPDMWSearchCriteria)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWSearchCriteria"
member: "AddCriteria"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~AddCriteria.html"
---

# AddCriteria Method (IPDMWSearchCriteria)

Adds a search criteria.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCriteria( _
   ByVal andOr As PDMWAndOr, _
   ByVal propertyType As PDMWPropertyType, _
   ByVal propertyName As System.String, _
   ByVal condition As PDMWConditionType, _
   ByVal Value As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWSearchCriteria
Dim andOr As PDMWAndOr
Dim propertyType As PDMWPropertyType
Dim propertyName As System.String
Dim condition As PDMWConditionType
Dim Value As System.String
Dim value As System.Boolean

value = instance.AddCriteria(andOr, propertyType, propertyName, condition, Value)
```

### C#

```csharp
System.bool AddCriteria(
   PDMWAndOr andOr,
   PDMWPropertyType propertyType,
   System.string propertyName,
   PDMWConditionType condition,
   System.string Value
)
```

### C++/CLI

```cpp
System.bool AddCriteria(
   PDMWAndOr andOr,
   PDMWPropertyType propertyType,
   System.String^ propertyName,
   PDMWConditionType condition,
   System.String^ Value
)
```

### Parameters

- `andOr`: Logical operator for subsequent criteria as defined in [PDMWAndOr](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.PDMWAndOr.html)
- `propertyType`: Property type as defined in [PDMWPropertyType](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.PDMWPropertyType.html)
- `propertyName`: Name of property to use with which to search
- `condition`: Search condition as defined in [PDMWConditionType](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.PDMWConditionType.html)
- `Value`: Value of the property for which to search

### Return Value

True if this search criteria is added, false if not

## VBA Syntax

See [PDMWSearchCriteria::AddCriteria](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWSearchCriteria~AddCriteria.html).

## Examples

[Create Search Criteria and Search Vault Example (VBA)](Create_Search_Criteria_and_Search_Vault_Example_VB.htm)

## See Also

[IPDMWSearchCriteria Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria.html)
[IPDMWSearchCriteria Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria_members.html)
[IPDMWSearchCriteria::GetCriteria Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~GetCriteria.html)
[IPDMWSearchCriteria::RemoveCriteria Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~RemoveCriteria.html)
[IPDMWSearchCriteria::LoadFromFile Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~LoadFromFile.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
