---
title: "GetSectionLineCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetSectionLineCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineCount.html"
---

# GetSectionLineCount Method (IView)

Obsolete. Superseded by [IView::GetSectionLineCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetSectionLineCount2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSectionLineCount( _
   ByRef Size As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Size As System.Integer
Dim value As System.Integer

value = instance.GetSectionLineCount(Size)
```

### C#

```csharp
System.int GetSectionLineCount(
   out System.int Size
)
```

### C++/CLI

```cpp
System.int GetSectionLineCount(
   [Out] System.int Size
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Size`:

## VBA Syntax

See [View::GetSectionLineCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetSectionLineCount.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
