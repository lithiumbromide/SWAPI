---
title: "SetSpringType Method (ICWSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSpringConnector"
member: "SetSpringType"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~SetSpringType.html"
---

# SetSpringType Method (ICWSpringConnector)

Sets the type of spring.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetSpringType( _
   ByVal NSpringType As System.Integer, _
   ByVal NSpringSubType As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSpringConnector
Dim NSpringType As System.Integer
Dim NSpringSubType As System.Integer

instance.SetSpringType(NSpringType, NSpringSubType)
```

### C#

```csharp
void SetSpringType(
   System.int NSpringType,
   System.int NSpringSubType
)
```

### C++/CLI

```cpp
void SetSpringType(
   System.int NSpringType,
   System.int NSpringSubType
)
```

### Parameters

- `NSpringType`: Spring type as defined in [swsSpringType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSpringType_e.html)
- `NSpringSubType`: Spring sub type as defined in [swsSpringSubType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSpringSubType_e.html)

## VBA Syntax

See [CWSpringConnector::SetSpringType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSpringConnector~SetSpringType.html).

## See Also

[ICWSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector.html)
[ICWSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector_members.html)
[ICWSpringConnector::GetSpringType Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~GetSpringType.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
