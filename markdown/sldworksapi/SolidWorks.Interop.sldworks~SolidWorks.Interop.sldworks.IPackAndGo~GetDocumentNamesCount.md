---
title: "GetDocumentNamesCount Method (IPackAndGo)"
project: "SOLIDWORKS API Help"
interface: "IPackAndGo"
member: "GetDocumentNamesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentNamesCount.html"
---

# GetDocumentNamesCount Method (IPackAndGo)

Gets the number of documents comprising the model for Pack and Go.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDocumentNamesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPackAndGo
Dim value As System.Integer

value = instance.GetDocumentNamesCount()
```

### C#

```csharp
System.int GetDocumentNamesCount()
```

### C++/CLI

```cpp
System.int GetDocumentNamesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of documents comprising the model

## VBA Syntax

See [PackAndGo::GetDocumentNamesCount](ms-its:sldworksapivb6.chm::/sldworks~PackAndGo~GetDocumentNamesCount.html).

## Examples

[Pack and Go an Assembly (C#)](Pack_and_Go_an_Assembly_Example_CSharp.htm)
[Pack and Go an Assembly (VB.NET)](Pack_and_Go_an_Assembly_Example_VBNET.htm)
[Pack and Go an Assembly (VBA)](Pack_and_Go_an_Assembly_Example_VB.htm)

## Remarks

Call this method before calling [IPackAndGo::IGetDocumentNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPackAndGo~IGetDocumentNames.html) and [IPackAndGo::IGetDocumentSaveToNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPackAndGo~IGetDocumentSaveToNames.html) to determine the size of the array for each method.

## See Also

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html)
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
