---
title: "IPunchTable Interface"
project: "SOLIDWORKS API Help"
interface: "IPunchTable"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable.html"
---

# IPunchTable Interface

Allows access to punch table information and values.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IPunchTable
```

### Visual Basic (Usage)

```vb
Dim instance As IPunchTable
```

### C#

```csharp
public interface IPunchTable
```

### C++/CLI

```cpp
public interface class IPunchTable
```

## VBA Syntax

See [PunchTable](ms-its:sldworksapivb6.chm::/sldworks~PunchTable.html).

## Examples

[Insert Punch Table (C#)](Insert_Punch_Table_Example_CSharp.htm)
[Insert Punch Table (VB.NET)](Insert_Punch_Table_Example_VBNET.htm)
[Insert Punch Table (VBA)](Insert_Punch_Table_Example_VB.htm)

## Remarks

Punch tables contain information about the punches that are created by forming tools in sheet metal parts. A punch table contains the following information about pre-selected punches:

| Column | Description |
| --- | --- |
| TAG | Datum tag added to each punch in the flat pattern view |
| PUNCH ID | Property of the forming tool or library feature |
| X Location | Distance from the x-axis to the point of insertion of the forming tool in the flat pattern view |
| Y Location | Distance from the y-axis to the point of insertion of the forming tool in the flat pattern view |
| ANGLE | Angle between the x-axis and the forming tool |
| QUANTITY | Number of times that the forming tool is used in the flat pattern view |

## Accessors

[IPunchTableAnnotation::PunchTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPunchTableAnnotation~PunchTable.html)

## Access Diagram

[PunchTable](SWObjectModel.pdf#PunchTable)

## See Also

[IPunchTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IPunchTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTableAnnotation.html)
[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
