---
title: "IGetMathUtility Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IGetMathUtility"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetMathUtility.html"
---

# IGetMathUtility Method (ISldWorks)

Gets the [IMathUtility](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathUtility.html) interface.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMathUtility() As MathUtility
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As MathUtility

value = instance.IGetMathUtility()
```

### C#

```csharp
MathUtility IGetMathUtility()
```

### C++/CLI

```cpp
MathUtility^ IGetMathUtility();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IMathUtility](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathUtility.html) or NULL if the operation fails

## VBA Syntax

See [SldWorks::IGetMathUtility](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IGetMathUtility.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetMathUtility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMathUtility.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
