package com.example.android.wearable.composeforwearos

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.wrapContentSize
import androidx.compose.material.icons.Icons
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.wear.compose.material.AutoCenteringParams
import androidx.wear.compose.material.PositionIndicator
import androidx.wear.compose.material.Scaffold
import androidx.wear.compose.material.ScalingLazyColumn
import androidx.wear.compose.material.TimeText
import androidx.wear.compose.material.Vignette
import androidx.wear.compose.material.VignettePosition
import androidx.wear.compose.material.rememberScalingLazyListState
import androidx.wear.compose.material.scrollAway
import com.example.android.wearable.composeforwearos.theme.WearAppTheme
import androidx.compose.material.icons.rounded.*
import com.google.firebase.database.DataSnapshot
import com.google.firebase.database.DatabaseError
import com.google.firebase.database.FirebaseDatabase
import com.google.firebase.database.ValueEventListener
import com.google.firebase.database.ktx.getValue

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        fun sendCommand(nombreClave: String) {
            val ref = FirebaseDatabase.getInstance().getReference("Devices/$nombreClave")
            val listener = object : ValueEventListener {
                override fun onDataChange(snapshot: DataSnapshot) {
                    val valorActual = snapshot.getValue<Boolean>()
                    val nuevoValor = valorActual?.not() ?: true
                    ref.setValue(nuevoValor)
                    ref.removeEventListener(this)
                }
                override fun onCancelled(error: DatabaseError) {
                    println("Error al leer el valor de $nombreClave: ${error.message}")
                    ref.removeEventListener(this)
                }
            }
            ref.addValueEventListener(listener)
        }
        fun sendCommandOFF(nombreClave: String) {
            val ref = FirebaseDatabase.getInstance().getReference("Devices/$nombreClave")
            val listener = object : ValueEventListener {
                override fun onDataChange(snapshot: DataSnapshot) {
                    ref.setValue(true)
                    ref.removeEventListener(this)
                }
                override fun onCancelled(error: DatabaseError) {
                    println("Error al leer el valor de $nombreClave: ${error.message}")
                    ref.removeEventListener(this)
                }
            }
            ref.addValueEventListener(listener)
        }
        fun sendCommandOFFALL() {
            sendCommandOFF("Desk Lights")
            sendCommandOFF("Central Lights")
            sendCommandOFF("Room Lights")
            sendCommandOFF("Speaker")
            sendCommandOFF("LEDs RGB")
            sendCommandOFF("PC")
            sendCommandOFF("3D Printer")
            sendCommandOFF("AAC")
        }
        fun onPause() {
            super.onPause()
            finish()
        }
        setContent {
            WearAppTheme {
                val listState = rememberScalingLazyListState()
                Scaffold(
                    timeText = {
                        TimeText(modifier = Modifier.scrollAway(listState))
                    },
                    vignette = {
                        Vignette(vignettePosition = VignettePosition.TopAndBottom)
                    },
                    positionIndicator = {
                        PositionIndicator(
                            scalingLazyListState = listState
                        )
                    }
                ) {
                    val contentModifier = Modifier
                        .fillMaxWidth()
                        .padding(bottom = 8.dp)
                    val iconModifier = Modifier
                        .size(24.dp)
                        .wrapContentSize(align = Alignment.Center)
                    ScalingLazyColumn(
                        modifier = Modifier.fillMaxSize(),
                        autoCentering = AutoCenteringParams(itemIndex = 0),
                        state = listState
                    ) {
                        item { ChipExample(contentModifier,iconModifier,"Desk Lights" , Icons.Rounded.AlignHorizontalLeft,function = {sendCommand("Desk Lights")}) }
                        item { ChipExample(contentModifier,iconModifier,"Central Lights",Icons.Rounded.AlignHorizontalCenter,function = {sendCommand("Central Lights")}) }
                        item { ChipExample(contentModifier,iconModifier,"Room Lights",Icons.Rounded.Light,function = {sendCommand("Room Lights")}) }
                        item { ChipExample(contentModifier,iconModifier,"Speaker",Icons.Rounded.Speaker,function = {sendCommand("Speaker")}) }
                        item { ChipExample(contentModifier,iconModifier,"LEDs RGB",Icons.Rounded.LightMode,function = {sendCommand("LEDs RGB")}) }
                        item { ChipExample(contentModifier,iconModifier,"PC",Icons.Rounded.Computer,function = {sendCommand("PC")})}
                        item { ChipExample(contentModifier,iconModifier,"3D Printer",Icons.Rounded.Print,function = {sendCommand("3D Printer")}) }
                        item { ChipExample(contentModifier,iconModifier,"AAC",Icons.Rounded.Air,function = {sendCommand("AAC")}) }
                        item { ButtonExample(contentModifier,iconModifier,function = {sendCommandOFFALL()})
                        }
                    }
                }
            }
        }
    }
}



