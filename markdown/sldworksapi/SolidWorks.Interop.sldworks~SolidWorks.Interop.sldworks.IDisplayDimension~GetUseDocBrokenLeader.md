---
title: "GetUseDocBrokenLeader Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetUseDocBrokenLeader"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocBrokenLeader.html"
---

# GetUseDocBrokenLeader Method (IDisplayDimension)

Gets whether this display dimension uses the document default setting for displaying leaders as broken.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUseDocBrokenLeader() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

value = instance.GetUseDocBrokenLeader()
```

### C#

```csharp
System.bool GetUseDocBrokenLeader()
```

### C++/CLI

```cpp
System.bool GetUseDocBrokenLeader();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this display dimension uses the document setting, false if it uses a specific setting

## VBA Syntax

See [DisplayDimension::GetUseDocBrokenLeader](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetUseDocBrokenLeader.html).

## Remarks

SOLIDWORKS can display dimension text above a solid, unbroken leader line, or the dimension leader line can be broken with the text displayed either horizontal or aligned with the leader line. This method allows you to determine if this [IDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html) is using the document default setting for this value or if the user has applied a
specific setting to this specific IDisplayDimension.

Use [IDisplayDimension::SetBrokenLeader2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~SetBrokenLeader2.html) to set this value.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetBrokenLeader2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetBrokenLeader2.html)
[IDisplayDimension::SolidLeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SolidLeader.html)

## Availability

SOLIDWORKS 99, datecode 1999207
