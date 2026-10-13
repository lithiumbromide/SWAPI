---
title: "IGetSheetNames Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "IGetSheetNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetSheetNames.html"
---

# IGetSheetNames Method (IDrawingDoc)

Gets a list of the names of the drawing sheets in this drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSheetNames( _
   ByRef Count As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Count As System.Integer
Dim value As System.String

value = instance.IGetSheetNames(Count)
```

### C#

```csharp
System.string IGetSheetNames(
   out System.int Count
)
```

### C++/CLI

```cpp
System.String^ IGetSheetNames(
   [Out] System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of drawing sheets in this drawing (see Remarks)

### Return Value

- in-process, unmanaged C++: Pointer to an array containing the names of the drawing sheets in this drawing of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The argument Count is used to help prevent memory overwrites. First call [IDrawingDoc::GetSheetCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~GetSheetCount.html) to get the number of sheets in this drawing. Then use its return value to dimension the return value array.

This method compares the number of sheets in this part with the value passed in.

| If the actual number of sheets is... | Then... |
| --- | --- |
| Larger than the value passed in | no sheets are returned, and status returns S_ERROR. |
| Smaller than this value | the names of all of the sheets in the return value is returned and changes Count to reflect the actual number of sheets. |

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::ActivateSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateSheet.html)
[IDrawingDoc::EditSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet.html)
[IDrawingDoc::GetCurrentSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetCurrentSheet.html)
[IDrawingDoc::GetSheetNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetNames.html)
[IDrawingDoc::IGetCurrentSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetCurrentSheet.html)
[IDrawingDoc::NewSheet3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewSheet3.html)
[IDrawingDoc::SetupSheet4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet4.html)
[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
