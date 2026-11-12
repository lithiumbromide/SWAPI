---
title: "SetHeader Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "SetHeader"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetHeader.html"
---

# SetHeader Method (ITableAnnotation)

Sets the header for this table.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetHeader( _
   ByVal Style As System.Integer, _
   ByVal Count As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Style As System.Integer
Dim Count As System.Integer
Dim value As System.Boolean

value = instance.SetHeader(Style, Count)
```

### C#

```csharp
System.bool SetHeader(
   System.int Style,
   System.int Count
)
```

### C++/CLI

```cpp
System.bool SetHeader(
   System.int Style,
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Style`: Header style as defined in [swTableHeaderPosition_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableHeaderPosition_e.html)
- `Count`: Number of lines in the header

### Return Value

True if header is set successfully, false if not

## VBA Syntax

See [TableAnnotation::SetHeader](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~SetHeader.html).

## Remarks

Tables created internally by the SOLIDWORKS Design software, such as Hole Charts, Revision Blocks, and BOM tables, are created with a specific number of headers lines.

This method cannot:

- Change the number of lines in the header for these tables; thus, the Count argument is ignored.
- Turn off the header in these types of tables; thus, this method has no effect, and FALSE is returned.

Essentially, the only thing this method can do with these types of tables is to change the header between the top and the bottom.

If you are changing the header style and number of header lines in a single use of this method, the number of lines is considered before changing the header style. For example, if you are changing a table that had 1 header line at the top, by calling SetHeader (swTableHeader_Bottom, 3), the first 3 lines in the table are moved to the bottom of the table.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetHeaderCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetHeaderCount.html)
[ITableAnnotation::GetHeaderStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetHeaderStyle.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
