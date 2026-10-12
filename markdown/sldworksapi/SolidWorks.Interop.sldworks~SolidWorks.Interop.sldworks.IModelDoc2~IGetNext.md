---
title: "IGetNext Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IGetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetNext.html"
---

# IGetNext Method (IModelDoc2)

Gets the next document opened in the current SOLIDWORKS Design session.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNext() As ModelDoc2
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As ModelDoc2

value = instance.IGetNext()
```

### C#

```csharp
ModelDoc2 IGetNext()
```

### C++/CLI

```cpp
ModelDoc2^ IGetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next [model document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) opened in the current SOLIDWORKS Design session

## VBA Syntax

See [ModelDoc2::IGetNext](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IGetNext.html).

## Remarks

To traverse all documents open in this SOLIDWORKS Design session, the first IModleDoc2 object that calls this method must have been returned from [ISldWorks::IGetFirstDocument2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IGetFirstDocument2.html).

**NOTE:** This method is available in datecode 1999/207 and later.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetNext.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
