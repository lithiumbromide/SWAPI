---
title: "GetLastErrorCode Method (ICWBearingConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingConnector"
member: "GetLastErrorCode"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~GetLastErrorCode.html"
---

# GetLastErrorCode Method (ICWBearingConnector)

Gets the last error thrown for this bearing connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLastErrorCode() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingConnector
Dim value As System.Integer

value = instance.GetLastErrorCode()
```

### C#

```csharp
System.int GetLastErrorCode()
```

### C++/CLI

```cpp
System.int GetLastErrorCode();
```

### Return Value

Error code as defined by [swsBearingConnectorErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBearingConnectorErrors_e.html)

## VBA Syntax

See [CWBearingConnector::GetLastErrorCode](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingConnector~GetLastErrorCode.html).

## See Also

[ICWBearingConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html)
[ICWBearingConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2024 SP0
