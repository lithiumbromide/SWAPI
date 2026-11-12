---
title: "ModelName Property (IEntity)"
project: "SOLIDWORKS API Help"
interface: "IEntity"
member: "ModelName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~ModelName.html"
---

# ModelName Property (IEntity)

Gets or sets the standard Parasolid name attribute of the entity.

## Syntax

### Visual Basic (Declaration)

```vb
Property ModelName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IEntity
Dim value As System.String

instance.ModelName = value

value = instance.ModelName
```

### C#

```csharp
System.string ModelName {get; set;}
```

### C++/CLI

```cpp
property System.String^ ModelName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Standard Parasolid name attribute

## VBA Syntax

See [Entity::ModelName](ms-its:sldworksapivb6.chm::/sldworks~Entity~ModelName.html).

## Examples

This Visual Basic subroutine shows how to write a Parasolid name attribute to each face in the model.

```vb
Private Sub NameAllFaces (ByRef swBody as SldWorks.body2)
```

```vb
Dim swFace as Sldworks.Face2
Dim swEnt As Sldworks.Entity
Dim Name, RootName As String
Dim Index As Integer
Dim ret as Boolean
```

```vb
swFace = swBody.GetFirstFace

Index = 0
RootName = "My Face #"

Do While Not swFace is Nothing
```

```vb
swEnt = swFace
Name = RootName + str(Index)
swEnt.ModelName = Name
Index = Index + 1
swFace = swFace.GetNextFace
```

```vb
Loop
```

```vb
End Sub
```

## See Also

[IEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.html)
[IEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity_members.html)
