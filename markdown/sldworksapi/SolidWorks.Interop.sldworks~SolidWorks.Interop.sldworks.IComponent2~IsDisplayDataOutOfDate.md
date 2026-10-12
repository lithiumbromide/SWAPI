---
title: "IsDisplayDataOutOfDate Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IsDisplayDataOutOfDate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsDisplayDataOutOfDate.html"
---

# IsDisplayDataOutOfDate Method (IComponent2)

Gets the status of the display data for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsDisplayDataOutOfDate() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Integer

value = instance.IsDisplayDataOutOfDate()
```

### C#

```csharp
System.int IsDisplayDataOutOfDate()
```

### C++/CLI

```cpp
System.int IsDisplayDataOutOfDate();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Rebuild state of the components as defined in [swOutOfDateStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swOutOfDateStatus_e.html)

## VBA Syntax

See [Component2::IsDisplayDataOutOfDate](ms-its:sldworksapivb6.chm::/sldworks~Component2~IsDisplayDataOutOfDate.html).

## Remarks

Tessellation information is available only when the component is loaded as lightweight.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
