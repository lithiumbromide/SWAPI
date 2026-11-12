---
title: "IGetEnvironment Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IGetEnvironment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetEnvironment.html"
---

# IGetEnvironment Method (ISldWorks)

Gets the [IEnvironment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnvironment.html) object.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEnvironment() As Environment
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As Environment

value = instance.IGetEnvironment()
```

### C#

```csharp
Environment IGetEnvironment()
```

### C++/CLI

```cpp
Environment^ IGetEnvironment();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IEnvironment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnvironment.html) object

## VBA Syntax

See [SldWorks::IGetEnvironment](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IGetEnvironment.html).

## Remarks

All numeric values returned from the IEnvironment object are relative to a unit text height of 1.0; i.e., if a symbol has a text height of 0.15, then you the numeric values returned by 0.15.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetEnvironment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetEnvironment.html)
