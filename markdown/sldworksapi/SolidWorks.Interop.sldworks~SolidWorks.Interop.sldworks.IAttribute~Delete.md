---
title: "Delete Method (IAttribute)"
project: "SOLIDWORKS API Help"
interface: "IAttribute"
member: "Delete"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~Delete.html"
---

# Delete Method (IAttribute)

Deletes an attribute and lets you indicate whether or not to update the FeatureManager design tree if the deleted attribute appears in it.

## Syntax

### Visual Basic (Declaration)

```vb
Function Delete( _
   ByVal BuildTree As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAttribute
Dim BuildTree As System.Boolean
Dim value As System.Boolean

value = instance.Delete(BuildTree)
```

### C#

```csharp
System.bool Delete(
   System.bool BuildTree
)
```

### C++/CLI

```cpp
System.bool Delete(
   System.bool BuildTree
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BuildTree`: True to update the FeatureManager design tree, false to not

### Return Value

True if the attribute is deleted, false if not

## VBA Syntax

See [Attribute::Delete](ms-its:sldworksapivb6.chm::/sldworks~Attribute~Delete.html).

## Examples

[Delete Faces (VBA)](Delete_Faces_Example_VB.htm)
[Delete Attribute (C#)](Delete_Attribute_Example_CSharp.htm)
[Delete Attribute (VB.NET)](Delete_Attribute_Example_VBNET.htm)
[Delete Attribute (VBA)](Delete_Attribute_Example_VB.htm)
[Delete Blended Faces (C#)](Delete_Blended_Faces_Example_CSharp.htm)
[Delete Blended Faces (VB.NET)](Delete_Blended_Faces_Example_VBNET.htm)
[Delete Blended Faces (VBA)](Delete_Blended_Faces_Example_VB.htm)

## See Also

[IAttribute Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.html)
[IAttribute Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
