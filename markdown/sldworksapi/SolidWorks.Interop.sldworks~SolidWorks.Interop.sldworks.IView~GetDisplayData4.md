---
title: "GetDisplayData4 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDisplayData4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayData4.html"
---

# GetDisplayData4 Method (IView)

Gets the the [IDisplayData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData.html) object for this drawing view containing only those model items that are visible in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayData4() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetDisplayData4()
```

### C#

```csharp
System.object GetDisplayData4()
```

### C++/CLI

```cpp
System.Object^ GetDisplayData4();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IDisplayData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData.html)

## VBA Syntax

See [View::GetDisplayData4](ms-its:sldworksapivb6.chm::/sldworks~View~GetDisplayData4.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
