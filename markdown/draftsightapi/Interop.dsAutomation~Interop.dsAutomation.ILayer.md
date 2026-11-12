---
title: "ILayer Interface"
project: ""
interface: "ILayer"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer.html"
---

# ILayer Interface

Allows access to a Layer.

## Syntax

### Visual Basic

```vb
Public Interface ILayer
```

### C#

```csharp
public interface ILayer
```

### JScript

```
public interface ILayer
```

### Managed Extensions for C++

```
public __gc __interface ILayer
```

### C++/CLI

```cpp
public interface class ILayer
```

## Examples

##### COM native C++

If the selected object is an ILayer object, then get the object.

...

//Write number of selected objects to output file
long selCount = dsSelManager->GetSelectedObjectCount( dsSelectionSetType_Current );
strPrint.Format( L"Selected objects: (%d):\r\n", selCount );
fileOutput.WriteString( strPrint );

if( selCount > 0 )
{
for( long i = 0; i < selCount; ++i )
{
//Get selected object type
dsObjectType_e retObjType;
IDispatchPtr selObj = dsSelManager->GetSelectedObject( dsSelectionSetType_Current, i, &retObjType );

//If selected object is a Layer entity
if(dsLayerType == retObjType )
{
ILayerPtr dsLayer( selObj );

strPrint.Format( L"Layer\r\n" );
fileOutput.WriteString( strPrint );

//Do dump for Layer entity

//See the entity's [LineStyle](Interop.dsAutomation~Interop.dsAutomation.ILayer~LineStyle.html) or [LineWeight](Interop.dsAutomation~Interop.dsAutomation.ILayer~LineWeight.html)
//property for the DumpGraphicsEntity template
CAddinDumpManager::DumpGraphicsEntity<ILayerPtr>( dsLayer, fileOutput );

...

## Examples

[Get and Set Hatch Pattern Data (C#)](Get_and_Set_Hatch_Pattern_Data_Example_CSharp.htm)
[Get and Set Hatch Pattern Data (VB.NET)](Get_and_Set_Hatch_Pattern_Data_Example_VBNET.htm)
[Get and Set Hatch Pattern Data (VBA)](Get_and_Set_Hatch_Pattern_Data_Example_VBA.htm)
[Create Circles on Different Layers (JavaScript)](Create_Circles_on_Different_Layers_Example_JS.htm)

## Accessors

Interop.dsAutomation~Interop.dsAutomation.IApplication~GetRGBColor.html

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

[ILayerManager::CreateLayer](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~CreateLayer.html)

[ILayerManager::GetActiveLayer](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~GetActiveLayer.html)

[ILayerManager::GetLayer](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~GetLayer.html)

[ILayerManager::GetLayers](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~GetLayers.html)

[ILayerState::GetLayers](Interop.dsAutomation~Interop.dsAutomation.ILayerState~GetLayers.html)

## Access Diagram

DSObjectModel.pdf#Layer

[Layer](DSObjectModel.pdf#Layer)

## See Also

[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[ILayerManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerManager.html)
