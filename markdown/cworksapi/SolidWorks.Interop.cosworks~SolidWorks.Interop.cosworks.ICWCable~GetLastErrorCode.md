---
title: "GetLastErrorCode Method (ICWCable)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCable"
member: "GetLastErrorCode"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable~GetLastErrorCode.html"
---

# GetLastErrorCode Method (ICWCable)

Gets the last error thrown for this cable connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLastErrorCode() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCable
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

Error code as defined by [swsCableEndEditErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCableEndEditErrors_e.html)

## VBA Syntax

See [CWCable::GetLastErrorCode](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCable~GetLastErrorCode.html).

## See Also

[ICWCable Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html)
[ICWCable Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable_members.html)

## Availability

SOLIDWORKS Simulation API 2026 SP0
