---
title: "IAttributeDef Interface"
project: "SOLIDWORKS API Help"
interface: "IAttributeDef"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.html"
---

# IAttributeDef Interface

Allows access to an attribute definition.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IAttributeDef
```

### Visual Basic (Usage)

```vb
Dim instance As IAttributeDef
```

### C#

```csharp
public interface IAttributeDef
```

### C++/CLI

```cpp
public interface class IAttributeDef
```

## VBA Syntax

See [AttributeDef](ms-its:sldworksapivb6.chm::/sldworks~AttributeDef.html).

## Examples

[Create Attribute (VBA)](Create_Attribute_Example_VB.htm)
[Add Attribute to Feature and Include in Library Feature (C#)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_CSharp.htm)
[Add Attribute to Feature and Include in Library Feature (VB.NET)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_VBNET.htm)
[Add Attribute to Feature and Include in Library Feature (VBA)](Add_Attribute_to_Feature_and_Include_In_Library_Feature_Example_VB.htm)

## Remarks

An attribute definition is an application-specific data packet that is automatically saved with the SOLIDWORKS file and reloaded when the file is opened. An application can create [attribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html) data that is attached to an entity in a SOLIDWORKS document.

The attribute definition describes a template for the data packet. The definition contains the names of the parameters in the attribute, their types and default values. It also allows you to create instances of the definition on entities in your model.

The general sequence of steps in IAttribute creation is to:

1. Create an attribute definition ([ISldWorks::DefineAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~DefineAttribute.html))
2. Add parameters to the attribute definition ([IAttributeDef::AddParameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef~AddParameter.html))
3. Register the attribute definition ([IAttributeDef::Register](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef~Register.html))
4. Create instances of the attribute definition on objects throughout the model ([IAttributeDef::CreateInstance5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef~CreateInstance5.html))

Perform Steps 1 through 3 only once for each working session. In other words, perform Steps 1 through 3 when your DLL or EXE is initially loaded or run. Until the DLL is unloaded or the EXE is closed, you can create an unlimited number of instances of the attribute definition.

## Accessors

[IAttribute::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute~GetDefinition.html) and [IAttribute::IGetDefinition Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute~IGetDefinition.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef|c3697' designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef|c3697'

[ISldWorks::DefineAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~DefineAttribute.html) and [ISldWorks::IDefineAttribute Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IDefineAttribute.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef|c3701' designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef|c3701'

## Access Diagram

[AttributeDef](SWObjectModel.pdf#AttributeDef)

## See Also

[IAttributeDef Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
