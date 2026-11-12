---
title: "InsertBendTableNew Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertBendTableNew"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBendTableNew.html"
---

# InsertBendTableNew Method (IModelDoc2)

Inserts a new bend table into the model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertBendTableNew( _
   ByVal FileName As System.String, _
   ByVal Units As System.String, _
   ByVal Type As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim FileName As System.String
Dim Units As System.String
Dim Type As System.String
Dim value As System.Boolean

value = instance.InsertBendTableNew(FileName, Units, Type)
```

### C#

```csharp
System.bool InsertBendTableNew(
   System.string FileName,
   System.string Units,
   System.string Type
)
```

### C++/CLI

```cpp
System.bool InsertBendTableNew(
   System.String^ FileName,
   System.String^ Units,
   System.String^ Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: File name of this new bend table
- `Units`: - Millimeters
  - Centimeters
  - Meters
  - Inches
  - Feet
- `Type`: - Bend Allowance
  - Bend Deduction

### Return Value

True if the new table is successfully inserted, false if not

## VBA Syntax

See [ModelDoc2::InsertBendTableNew](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertBendTableNew.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::DeleteBendTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteBendTable.html)
[IModelDoc2::InsertBendTableEdit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBendTableEdit.html)
[IModelDoc2::InsertBendTableOpen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBendTableOpen.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
