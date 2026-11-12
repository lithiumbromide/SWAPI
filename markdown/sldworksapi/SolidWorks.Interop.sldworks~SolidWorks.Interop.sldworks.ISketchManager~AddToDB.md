---
title: "AddToDB Property (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "AddToDB"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddToDB.html"
---

# AddToDB Property (ISketchManager)

Gets or sets whether sketch entities are added directly to the SOLIDWORKS database.

## Syntax

### Visual Basic (Declaration)

```vb
Property AddToDB As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim value As System.Boolean

instance.AddToDB = value

value = instance.AddToDB
```

### C#

```csharp
System.bool AddToDB {get; set;}
```

### C++/CLI

```cpp
property System.bool AddToDB {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to add items directly to the SOLIDWORKS database, false to not

## VBA Syntax

See [SketchManager::AddToDb](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~AddToDB.html).

## Examples

[Get Assembly Bounding Box Using Components (C#)](Get_Assembly_Bounding_Box_Using_Components_Example_CSharp.htm)
[Get Assembly Bounding Box Using Components (VB.NET)](Get_Assembly_Bounding_Box_Using_Components_Example_VBNET.htm)
[Get Assembly Bounding Box Using Components (VBA)](Get_Assembly_Bounding_Box_using_Components_Example_VB.htm)

## Remarks

One of the benefits of adding sketch entities directly to the database is that you can avoid grid and entity snapping. For example, if you create a sketch line whose endpoint is near another entity or grid point, the new sketch line endpoint snaps to the other entity or grid point. Setting this property to true avoids this behavior during sketch entity creation.

After setting this property to true:

- It is not possible to undo the creation of some types of sketch entities.
- You must reset it to false to restore SOLIDWORKS' normal operating mode.

This property and [ISketchManager::DisplayWhenAdded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~DisplayWhenAdded.html) improve performance during sketch entity creation. ISketchManager::DisplayWhenAdded requires that this property be set to true.

If you want to constrain all the sketch entities after creation, use [ISketch::ConstrainAll](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~ConstrainAll.html).

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
