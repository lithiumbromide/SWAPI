---
title: "IRay Interface"
project: ""
interface: "IRay"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRay.html"
---

# IRay Interface

Allows access to a Ray.

## Syntax

### Visual Basic

```vb
Public Interface IRay
```

### C#

```csharp
public interface IRay
```

### JScript

```
public interface IRay
```

### Managed Extensions for C++

```
public __gc __interface IRay
```

### C++/CLI

```cpp
public interface class IRay
```

## Examples

##### COM native C++

If the selected object is an IRay object, then get the object.

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

//If selected object is an Ray entity
if(dsRayType == retObjType )
{
IRayPtr dsRay( selObj );

strPrint.Format( L"Ray\r\n" );
fileOutput.WriteString( strPrint );

//Do dump for Ray entity

//See the entity's [Layer](Interop.dsAutomation~Interop.dsAutomation.IRay~Layer.html), [LineScale](Interop.dsAutomation~Interop.dsAutomation.IRay~LineScale.html), [LineStyle](Interop.dsAutomation~Interop.dsAutomation.IRay~LineStyle.html), [LineWeight](Interop.dsAutomation~Interop.dsAutomation.IRay~LineWeight.html),
//or [Visible](Interop.dsAutomation~Interop.dsAutomation.IRay~Visible.html) property for the DumpGraphicsEntity template
CAddinDumpManager::DumpGraphicsEntity<IRayPtr>( dsRay, fileOutput );

...

## Examples

[Insert Ray (C#)](Insert_Ray_Example_CSharp.htm)
[Insert Ray (VB.NET)](Insert_Ray_Example_VBNET.htm)
[Insert Ray (VBA)](Insert_Ray_Example_VBA.htm)

## Accessors

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

[ISelectionManager::GetSelectedObject](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

[ISelectionManager::GetSelectedObjects](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)

[ISketchManager::GetEntities](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)

[ISketchManager::InsertRay](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertRay.html)

## Access Diagram

DSObjectModel.pdf#Ray

[Ray](DSObjectModel.pdf#Ray)

## See Also

[IRay Members](Interop.dsAutomation~Interop.dsAutomation.IRay_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IInfiniteLine Interface](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine.html)
[ILine Interface](Interop.dsAutomation~Interop.dsAutomation.ILine.html)
[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[ITrace Interface](Interop.dsAutomation~Interop.dsAutomation.ITrace.html)
