---
title: "GetSpringType Method (ICWSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSpringConnector"
member: "GetSpringType"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~GetSpringType.html"
---

# GetSpringType Method (ICWSpringConnector)

Gets the type of spring.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetSpringType( _
   ByRef NSpringType As System.Integer, _
   ByRef NSpringSubType As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSpringConnector
Dim NSpringType As System.Integer
Dim NSpringSubType As System.Integer

instance.GetSpringType(NSpringType, NSpringSubType)
```

### C#

```csharp
void GetSpringType(
   out System.int NSpringType,
   out System.int NSpringSubType
)
```

### C++/CLI

```cpp
void GetSpringType(
   [Out] System.int NSpringType,
   [Out] System.int NSpringSubType
)
```

### Parameters

- `NSpringType`: Spring type as defined in [swsSpringType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSpringType_e.html)
- `NSpringSubType`: Spring sub type as defined in [swsSpringSubType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSpringSubType_e.html)

## VBA Syntax

See [CWSpringConnector::GetSpringType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSpringConnector~GetSpringType.html).

## Examples

See the [ICWSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector.html) examples.

## See Also

[ICWSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector.html)
[ICWSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector_members.html)
[ICWSpringConnector::SetSpringType Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~SetSpringType.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
