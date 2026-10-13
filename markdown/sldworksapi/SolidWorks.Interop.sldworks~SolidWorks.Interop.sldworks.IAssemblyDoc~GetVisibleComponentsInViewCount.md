---
title: "GetVisibleComponentsInViewCount Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "GetVisibleComponentsInViewCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetVisibleComponentsInViewCount.html"
---

# GetVisibleComponentsInViewCount Method (IAssemblyDoc)

Gets the number of visible components in this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVisibleComponentsInViewCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Integer

value = instance.GetVisibleComponentsInViewCount()
```

### C#

```csharp
System.int GetVisibleComponentsInViewCount()
```

### C++/CLI

```cpp
System.int GetVisibleComponentsInViewCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of visible components in this assembly

## VBA Syntax

See [AssemblyDoc::GetVisibleComponentsInViewCount](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~GetVisibleComponentsInViewCount.html).

## Remarks

Call this method before calling [IAssembly_Doc::IGetVisibleComponentsInView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~IGetVisibleComponentsInView.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
