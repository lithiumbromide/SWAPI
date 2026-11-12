---
title: "IGetExtent Method (IBomTable)"
project: "SOLIDWORKS API Help"
interface: "IBomTable"
member: "IGetExtent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~IGetExtent.html"
---

# IGetExtent Method (IBomTable)

Gets the lower-left and upper-right extents of the BOM on the drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetExtent() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTable
Dim value As System.Double

value = instance.IGetExtent()
```

### C#

```csharp
System.double IGetExtent()
```

### C++/CLI

```cpp
System.double IGetExtent();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

SOLIDWORKS returns the values in meters with respect to drawing sheet space.

The return value is the following array of doubles:

**[** `lowerLeftPt[3], upperRightPt[3]` **]**

where:

- lowerLeftPt[3] is an array of 3 doubles describing the X,Y,Z location for the lower-left corner of the BOM
- upperRightPt[3] is an array of 3 doubles describing the X,Y,Z location for the upper-right corner of the BOM

Before you use any of the IBomTable methods, activate the BOM table using [IBomTable::Attach3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~Attach3.html). After you finish getting BOM data, use [IBomTable::Detach](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable~Detach.html) to deactivate the table.

## See Also

[IBomTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.html)
[IBomTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable_members.html)
[IBomTable::GetExtent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~GetExtent.html)
