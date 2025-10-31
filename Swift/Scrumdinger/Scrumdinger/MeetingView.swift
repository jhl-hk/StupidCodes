//
//  ContentView.swift
//  Scrumdinger
//
//  Created by Jianyue Hugo Liang on 2025/10/31.
//

import SwiftUI

struct MeetingView: View {
    var body: some View {
        VStack {
            ProgressView(value: 5, total: 15)
            HStack {
                VStack(alignment: .leading) {
                    Text("Time Elapsed")
                        .font(.caption)
                    Label("300", systemImage: "hourglass.tophalf.fill")
                }
                Spacer()
                VStack(alignment: .trailing) {
                    Text("Time Remaining")
                        .font(.caption)
                    Label("300", systemImage: "hourglass.bottomhalf.fill")
                }
            }
            Circle()
                .strokeBorder(lineWidth: 24)
            HStack {
                Text("Speaker 1 of 3")
            }
        }
    }
}

#Preview {
    MeetingView()
}
